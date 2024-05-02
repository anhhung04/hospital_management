from repository.patient import PatientRepo
from fastapi import HTTPException, status
from models.patient import (
    PatientModel, PatientDetailModel,
    QueryPatientModel,
    AddPatientModel,
    PatchPatientModel,
    AddPatientRequestModel
)
from models.user import AddUserDetailModel, UserDetail
from models.medical_record import NewMedicalRecordModel, MedicalRecordModel
from models.patient_progress import (
    NewPatientProgressModel,
    QueryPatientProgressModel,
    ProgressRecordModel,
    PatchPatientProgressModel,
    PatientProgressDetailModel,
    PatientProgressInChargeModel
)
from models.employee import QueryEmployeeModel
from permissions import Permission
from permissions.user import UserRole
from repository.user import UserRepo, QueryUserModel
from repository.schemas.patient import MedicalRecord
from repository.schemas.patient import ProgressType
from util.crypto import PasswordContext
from uuid import uuid4
from fastapi import Depends
from middleware.user_ctx import UserContext
from datetime import datetime


class PatientService:
    def __init__(
        self,
        user: UserContext = Depends(UserContext),
        patient_repo: PatientRepo = Depends(PatientRepo),
        user_repo: UserRepo = Depends(UserRepo),
    ):
        self._current_user = user
        self._patient_repo = patient_repo
        self._user_repo = user_repo

    @Permission.permit([UserRole.EMPLOYEE])
    async def get_patients(self, page: int = 1, limit: int = 10):
        page, limit = abs(page) if page else 1, abs(limit)
        patients, err = await self._patient_repo.list_patient(page, limit)

        if err:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Error in get patients list'
            )
        try:
            patients = [
                PatientModel(
                    id=p.user_id,
                    full_name=" ".join(
                        [p.personal_info.last_name,
                            p.personal_info.first_name]
                    ),
                    phone_number=p.personal_info.phone_number,
                    medical_record_id=p.medical_record.id if p.medical_record else None,
                    appointment_date=self.find_appointment_date(
                        p.medical_record
                    )
                ).model_dump() for p in patients
            ]
        except Exception as err:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Error in convert patients list'
            )
        return patients

    @Permission.permit([UserRole.EMPLOYEE], acl=[UserRole.PATIENT])
    async def get(self, id: str, progress_page: int = 1, page_limit: int = 1):
        patient, err = await self._patient_repo.get(query=QueryPatientModel(
            user_id=id,
            progress_page=abs(progress_page),
            page_limit=abs(page_limit)
        ))
        if err:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Error in get patient infomation'
            )
        if not patient:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Patient not found'
            )
        appointment_date = None
        if patient.medical_record:
            appointment_date = PatientService.find_appointment_date(
                patient.medical_record
            )
        return PatientDetailModel(
            appointment_date=appointment_date,
            medical_record=MedicalRecordModel.model_validate(
                obj=patient.medical_record, strict=False, from_attributes=True
            ), personal_info=UserDetail.model_validate(
                obj=patient.personal_info, strict=False, from_attributes=True
            )
        ).model_dump()

    @Permission.permit([UserRole.EMPLOYEE])
    async def create(self, new_patient: AddPatientRequestModel):
        raw_password = PasswordContext.rand_key()
        username = f"patient_{new_patient.ssn}"
        user_info = new_patient.model_dump()
        patient_id = str(uuid4())
        user_info.update({
            "id": patient_id,
            "password": PasswordContext(raw_password, username).hash(),
            "username": username,
            "role": Permission(UserRole.PATIENT).get(),
        })
        patient_info = {
            "user_id": patient_id,
            "personal_info": AddUserDetailModel.model_validate(user_info).model_dump(),
            "medical_record": NewMedicalRecordModel(
                weight=0,
                height=0,
                note="",
                current_treatment="",
                drug_allergies="",
                food_allergies="",
                medical_history="",
            ).model_dump(),
        }
        patient_in_db, err = await self._patient_repo.create(
            AddPatientModel.model_validate(patient_info)
        )
        if patient_in_db:
            return {
                "username": patient_in_db.personal_info.username,
                "password": raw_password,
                "user_id": patient_in_db.user_id,
            }
        if err or not patient_in_db:
            raise HTTPException(
                status_code=500,
                detail='Error in create patient'
            )

    @Permission.permit([UserRole.EMPLOYEE])
    async def update(
        self,
        query: QueryPatientModel,
        patient_update: PatchPatientModel
    ):
        patient, err = await self._patient_repo.update(
            QueryPatientModel.model_validate(query),
            patient_update
        )
        if err:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Error in update patient infomation'
            )
        return PatientDetailModel(
            personal_info=UserDetail.model_validate(
                obj=patient.personal_info, strict=False, from_attributes=True
            ),
            medical_record=MedicalRecordModel.model_validate(
                obj=patient.medical_record, strict=False, from_attributes=True
            ),
            appointment_date=PatientService.find_appointment_date(
                patient.medical_record
            )
        ).model_dump()

    @Permission.permit([UserRole.EMPLOYEE])
    async def add_progress(
        self,
        query: QueryPatientProgressModel,
        progress: NewPatientProgressModel
    ):
        start_treatment = datetime.strptime(
            progress.start_treatment, '%Y-%m-%d %H:%M:%S'
        ) if progress.start_treatment else None
        end_treatment = datetime.strptime(
            progress.end_treatment, '%Y-%m-%d %H:%M:%S'
        ) if progress.end_treatment else None
        if start_treatment:
            if end_treatment:
                if end_treatment.__le__(start_treatment):
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail='End treatment must be greater than start treatment'
                    )
            current_time = datetime.now()
            if start_treatment.__le__(current_time):
                progress.status = ProgressType.PROCESSING
        progress, err = await self._patient_repo.create_progress(
            str(query.patient_id),
            progress
        )
        if err:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Error in add progress'
            )
        return ProgressRecordModel.model_validate(
            obj=progress, strict=False, from_attributes=True
        ).model_dump()

    @Permission.permit([UserRole.EMPLOYEE])
    async def update_progress(
        self,
        query: QueryPatientProgressModel,
        progress: PatchPatientProgressModel
    ):
        start_treatment = datetime.strptime(
            progress.start_treatment, '%Y-%m-%d %H:%M:%S'
        ) if progress.start_treatment else None
        end_treatment = datetime.strptime(
            progress.end_treatment, '%Y-%m-%d %H:%M:%S'
        ) if progress.end_treatment else None
        if start_treatment and end_treatment:
            if end_treatment.__le__(start_treatment):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail='End treatment must be greater than start treatment'
                )
        incharge_employees = []
        if progress.lead_employee and isinstance(progress.lead_employee, list):
            for employee in progress.lead_employee:
                if not employee.employee_email and not employee.employee_username:
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail='Employee email or username is required'
                    )
                incharge_user, err = await self._user_repo.get(
                    QueryUserModel(
                        email=employee.employee_email,
                        username=employee.employee_username
                    )
                )
                if err:
                    raise HTTPException(
                        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        detail='Error in get employee information'
                    )
                incharge_employees.append({
                    "employee_id": incharge_user.id,
                    "action": employee.action
                })
                progress.lead_employee = incharge_employees
        progress, err = await self._patient_repo.update_progress(
            query,
            progress
        )
        if err:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=err
            )
        lead_employee = [
            {
                "full_name": " ".join([
                    rel.employee.personal_info.last_name,
                    rel.employee.personal_info.first_name
                ]),
                "employee_email": rel.employee.personal_info.email,
                "action": rel.action
            } for rel in progress.lead_employee
        ]
        dump_progress = ProgressRecordModel.model_validate(
            obj=progress, strict=False, from_attributes=True
        ).model_dump()
        dump_progress.update({"lead_employee": lead_employee})
        return PatientProgressDetailModel.model_validate(
            dump_progress
        ).model_dump()

    @Permission.permit([UserRole.EMPLOYEE])
    async def get_progress(
        self,
        query: QueryPatientProgressModel,
    ):
        progress, err = await self._patient_repo.get_progress(
            query
        )
        if err:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=err
            )
        lead_employee = [
            {
                "full_name": " ".join([
                    rel.employee.personal_info.last_name,
                    rel.employee.personal_info.first_name
                ]),
                "employee_email": rel.employee.personal_info.email,
                "action": rel.action
            } for rel in progress.lead_employee
        ]
        dump_progress = ProgressRecordModel.model_validate(
            obj=progress, strict=False, from_attributes=True
        ).model_dump()
        dump_progress.update({"lead_employee": lead_employee})
        return PatientProgressDetailModel.model_validate(
            dump_progress
        ).model_dump()

    @Permission.permit([UserRole.EMPLOYEE])
    async def delete_lead_employee(
        self,
        query: QueryPatientProgressModel,
        delete_employee: QueryEmployeeModel
    ):
        employee, err = await self._user_repo.get(
            QueryUserModel(
                email=delete_employee.employee_email
            )
        )
        if err:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=err
            )
        progress, err = await self._patient_repo.delete_lead_employee(
            query,
            employee.id
        )
        if err:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=err
            )
        lead_employee = [
            {
                "full_name": " ".join([
                    rel.employee.personal_info.last_name,
                    rel.employee.personal_info.first_name
                ]),
                "employee_email": rel.employee.personal_info.email,
                "action": rel.action
            } for rel in progress.lead_employee]
        dump_progress = ProgressRecordModel.model_validate(
            obj=progress, strict=False, from_attributes=True
        ).model_dump()
        dump_progress.update({"lead_employee": lead_employee})
        return PatientProgressDetailModel.model_validate(
            dump_progress
        ).model_dump()

    @Permission.permit([UserRole.EMPLOYEE])
    async def get_progress_in_charge(self, patient_id, doctor_id, limit):
        if not doctor_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='Doctor id is required'
            )

        progress, err = await self._patient_repo.get_progress_in_charge(
            patient_id, doctor_id, limit
        )
        if err:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=err
            )
        return [
            PatientProgressInChargeModel.model_validate(
                obj=p, strict=False, from_attributes=True
            ).model_dump() for p in progress
        ]

    @staticmethod
    def find_appointment_date(media_record: MedicalRecord | None) -> str | None:
        if not media_record:
            return None
        progress = media_record.progress
        appointment_date = None
        if progress and isinstance(progress, list):
            progress = list(filter(
                lambda x: x and x.status == ProgressType.SCHEDULING,
                progress
            ))
            progress.sort(
                key=lambda x: x and x.start_treatment, reverse=True
            )
            if len(progress) > 0:
                latest_progress = progress[0]
                appointment_date = str(
                    latest_progress.start_treatment
                ) if latest_progress else None
        return appointment_date
