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
from models.medical_record import MedicalRecordModel
from permissions import Permission
from permissions.user import UserRole
from repository.user import UserRepo
from repository.schemas.patient import MedicalRecord
from repository.schemas.patient import Patient, ProgressType
from util.crypto import PasswordContext
from uuid import uuid4
from fastapi import Depends
from middleware.user_ctx import UserContext
from typing import Annotated


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

    @Permission.permit([UserRole.ADMIN, UserRole.EMPLOYEE])
    async def get_patients(self, page: int = 1, limit: int = 10):
        page, limit = abs(page) if page else 1, abs(limit)
        patients, err = await self._patient_repo.list_patient(page, limit)

        if err:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Error in get patients list'
            )
        try:
            def process_patient(patient: Patient):
                appointment_date = None
                if patient.medical_record:
                    appointment_date = PatientService.find_appointment_date(
                        patient.medical_record.progress
                    )
                return PatientModel(
                    id=patient.user_id,
                    full_name=" ".join(
                        [patient.personal_info.last_name,
                            patient.personal_info.first_name]
                    ),
                    phone_number=patient.personal_info.phone_number,
                    medical_record_id=patient.medical_record.id if patient.medical_record else None,
                    appointment_date=appointment_date
                ).model_dump()
            patients = [process_patient(p) for p in patients]
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Error in convert patients list'
            )
        return patients

    @Permission.permit([UserRole.ADMIN, UserRole.EMPLOYEE])
    async def get(self, query: QueryPatientModel):
        if Permission.has_role([UserRole.PATIENT], self._current_user):
            if self._current_user.id() != query.user_id:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail='Permission denied'
                )
        patient, err = await self._patient_repo.get(query)
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
                patient.medical_record.progress
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
        user_info.update({
            "id": str(uuid4()),
            "password": PasswordContext(raw_password, username).hash(),
            "username": username,
            "role": Permission(UserRole.PATIENT).get(),
        })
        user_in_db, err = await self._user_repo.create(
            AddUserDetailModel.model_validate(user_info)
        )
        if err:
            patient_info = {
                "user_id": err.params.get("id"),
            }
        else:
            patient_info = {
                "user_id": user_in_db.id,
            }
        patient_in_db, _ = await self._patient_repo.create(
            AddPatientModel.model_validate(patient_info)
        )
        if user_in_db and patient_in_db:
            return {
                "username": patient_in_db.personal_info.username,
                "password": raw_password,
                "user_id": patient_in_db.user_id,
            }
        if not user_in_db:
            raise HTTPException(
                status_code=500,
                detail='Error in create user'
            )
        if not patient_in_db:
            raise HTTPException(
                status_code=500,
                detail='Error in create patient'
            )

    @Permission.permit([UserRole.ADMIN, UserRole.EMPLOYEE])
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
                patient.medical_record.progress
            )
        ).model_dump()

    @staticmethod
    def find_appointment_date(media_record: MedicalRecord) -> str:
        if not media_record:
            return None
        progress = media_record.progress
        appointment_date = None
        if progress and len(progress) > 0:
            latest_progress = progress[-1]
            appointment_date = str(
                latest_progress.created_at
            ) if latest_progress and latest_progress.status == ProgressType.SCHEDULING else None
        return appointment_date
