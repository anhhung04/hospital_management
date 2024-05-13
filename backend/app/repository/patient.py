from repository.schemas.patient import Patient, MedicalRecord, PatientProgress, EmployeeHandlePatient, ProgressType
from repository.schemas.user import User
from sqlalchemy.sql import text, between, and_
from repository.user import UserRepo
from sqlalchemy.orm import Session, noload
from sqlalchemy.exc import IntegrityError
from typing import Tuple
from models.patient import QueryPatientModel, PatchPatientModel, AddPatientModel
from models.patient_progress import NewPatientProgressModel, QueryPatientProgressModel, PatchPatientProgressModel, PatientProgressInChargeModel
from repository import Storage
from fastapi import Depends
from datetime import datetime, timedelta

class PatientRepo:
    def __init__(
        self,
        userRepo: UserRepo = Depends(UserRepo),
        session: Session = Depends(Storage.get)
    ):
        self._sess = session
        self._user_repo = userRepo

    @staticmethod
    async def call():
        return PatientRepo()

    async def get(self, query: QueryPatientModel) -> Tuple[Patient, Exception | None]:
        try:
            patient = self._sess.query(Patient).filter(
                Patient.user_id == query.user_id
            ).options(
                noload(Patient.medical_record)
            ).first()
            medical_record = self._sess.query(MedicalRecord).filter(
                MedicalRecord.id == patient.medical_record_id
            ).options(
                noload(MedicalRecord.progress)
            ).first()
            progress = self._sess.query(PatientProgress).filter(
                PatientProgress.patient_id == query.user_id
            ).order_by(PatientProgress.id.desc()).subquery().alias("progress")
            progress = self._sess.query(progress).filter(
                progress.c.patient_id == query.user_id
            ).limit(
                query.page_limit
            ).offset(
                (query.progress_page - 1) * query.page_limit
            ).all()
            progress = [
                PatientProgress(
                    **{
                        c: getattr(p, c) for c in p._fields
                    }
                )
                for p in progress
            ]
            setattr(medical_record, "progress", progress)
            setattr(patient, "medical_record", medical_record)
        except Exception as err:
            return None, err
        return patient, None

    async def create(self, patient_info: AddPatientModel) -> Tuple[Patient, Exception | None]:
        try:
            new_patient = Patient(
                user_id=patient_info.user_id,
                personal_info=User(**patient_info.personal_info.model_dump()),
                medical_record=MedicalRecord(
                    **patient_info.medical_record.model_dump()
                )
            )
            self._sess.add(new_patient)
            self._sess.commit()
        except IntegrityError as err:
            self._sess.rollback()
            return None, err
        except Exception as err:
            return None, err
        return new_patient, None

    async def update(
        self,
        query: QueryPatientModel,
        patient_update: PatchPatientModel
    ) -> Tuple[Patient, Exception | None]:
        try:
            patient = self._sess.query(Patient).filter(
                Patient.user_id == query.user_id
            ).first()
            if not patient:
                return None, Exception("Patient not found")
            dump_update_patient = patient_update.model_dump()
            if dump_update_patient.get("personal_info"):
                for attr, value in dump_update_patient.get("personal_info", {}).items():
                    setattr(
                        patient.personal_info,
                        attr,
                        value
                    ) if value else None
            if dump_update_patient.get("medical_record"):
                for attr, value in dump_update_patient.get("medical_record", {}).items():
                    setattr(
                        patient.medical_record,
                        attr,
                        value
                    ) if value else None
            self._sess.add(patient)
            self._sess.commit()
            self._sess.refresh(patient)
        except Exception as err:
            self._sess.rollback()
            return None, err
        return patient, None

    async def list_patient(
        self,
        page: int,
        limit: int
    ) -> Tuple[list[Patient], Exception | None]:
        try:
            patients = self._sess.query(Patient).outerjoin(
                self._sess.query(MedicalRecord).filter(
                    MedicalRecord.id == Patient.medical_record_id
                ).outerjoin(
                    self._sess.query(PatientProgress).filter(
                        PatientProgress.medical_record_id == MedicalRecord.id
                    ).limit(1).subquery()
                ).subquery()
            ).limit(
                limit
            ).offset(
                (page - 1) * limit
            ).all()
        except Exception as err:
            return [], err
        return patients, None

    async def create_progress(
        self,
        patient_id: str,
        progress: NewPatientProgressModel
    ) -> Tuple[PatientProgress, Exception | None]:
        try:
            medical_record_id = self._sess.query(Patient.medical_record_id).filter(
                Patient.user_id == patient_id
            ).first().tuple()[0]
            if not medical_record_id:
                raise Exception("Medical record not found")
            new_progress = PatientProgress(
                medical_record_id=medical_record_id,
                patient_id=patient_id,
                **progress.model_dump()
            )
            self._sess.add(new_progress)
            self._sess.commit()
        except Exception as err:
            self._sess.rollback()
            return None, err
        return new_progress, None

    async def update_progress(
        self,
        query: QueryPatientProgressModel,
        progress: PatchPatientProgressModel
    ):
        try:
            patient_progress = self._sess.query(PatientProgress).filter(
                and_(
                    PatientProgress.id == query.progress_id,
                    PatientProgress.patient_id == query.patient_id
                )
            ).first()
            if not patient_progress:
                raise Exception("Patient progress not found")
            dump_update_progress = progress.model_dump()
            lead_employee = dump_update_progress.pop("lead_employee", None)
            for attr, value in dump_update_progress.items():
                setattr(patient_progress, attr, value) if value else None
            if lead_employee:
                for employee in lead_employee:
                    self._sess.execute(text("""
                        INSERT INTO in_charge_of_patients (progress_id, employee_id, action)
                        VALUES (:progress_id, :employee_id, :action);
                    """), {
                        "progress_id": query.progress_id,
                        "employee_id": employee.get("employee_id"),
                        "action": employee.get("action", "")
                    })
            self._sess.add(patient_progress)
            self._sess.commit()
            self._sess.refresh(patient_progress)
        except Exception as err:
            self._sess.rollback()
            return None, err
        return patient_progress, None

    async def get_progress(
        self,
        query: QueryPatientProgressModel
    ):
        try:
            patient_progress = self._sess.query(PatientProgress).filter(
                and_(
                    PatientProgress.id == query.progress_id,
                    PatientProgress.patient_id == query.patient_id
                )
            ).first()
        except Exception as err:
            return None, err
        return patient_progress, None

    async def delete_lead_employee(
        self,
        query: QueryPatientProgressModel,
        employee_id: str
    ):
        try:
            self._sess.execute(text("""
                DELETE FROM in_charge_of_patients
                WHERE progress_id = :id AND employee_id = :employee_id;
            """), {"id": query.progress_id, "employee_id": employee_id})
            self._sess.commit()
            newProgress, err = await self.get_progress(query)
            if err:
                return None, err
            return newProgress, None
        except Exception as err:
            self._sess.rollback()
            return None, err

    async def count(self):
        try:
            return self._sess.query(Patient).count(), None
        except Exception as err:
            return 0, err

    async def count_per_day(self, days: int):
        try:
            current_date = datetime.now()
            dates = [current_date - timedelta(days=i) for i in range(days)]
            counts = []
            for date in dates:
                count = self._sess.query(PatientProgress).filter(
                    between(PatientProgress.created_at,
                            date, date + timedelta(days=1))
                ).count()
                counts.append(count)
            return counts, None
        except Exception as err:
            return [], err

    async def get_progress_in_charge(self, doctor_id, limit):
        try:
            progress = self._sess.query(PatientProgress).filter(
                and_(
                    PatientProgress.lead_employee.any(
                        EmployeeHandlePatient.employee_id == doctor_id
                    ),
                    PatientProgress.status != ProgressType.FINISHED
                )
            ).order_by(PatientProgress.id.desc()).limit(limit).all()
            progress = [
                PatientProgressInChargeModel(
                    patient_id=p.patient_id,
                    employee_id=doctor_id,
                    patient_name=" ".join([
                        p.medical_record.patient.personal_info.first_name,
                        p.medical_record.patient.personal_info.last_name
                    ]),
                    status=str(p.status),
                    patient_condition=p.patient_condition,
                    start_treatment=p.start_treatment,
                    end_treatment=p.end_treatment
                )
                for p in progress
            ]
            return progress, None
        except Exception as err:
            return [], err
