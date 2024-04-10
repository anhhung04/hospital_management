from repository.schemas.patient import Patient, MedicalRecord, PatientProgress
from repository.schemas.user import User
from repository.user import UserRepo
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import Tuple
from models.patient import QueryPatientModel, PatchPatientModel, AddPatientModel
from models.patient_progress import NewPatientProgressModel
from repository import Storage
from fastapi import Depends

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
            ).outerjoin(
                self._sess.query(MedicalRecord).filter(
                    MedicalRecord.id == Patient.medical_record_id
                ).outerjoin(
                    self._sess.query(PatientProgress).filter(
                        PatientProgress.medical_record_id == MedicalRecord.id
                    ).limit(query.max_progress).subquery()
                ).subquery()
            ).first()
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
            patient, err = await self.get(query)
            if err:
                return None, err
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
        patient_id: int,
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
