from services import IService
from permissions import Permission
from permissions.user import UserRole
from models.medical_record import (
    MedicalRecordModel, QueryMedicalRecordModel,
    NewMedicalRecordModel, PatchMedicalRecordModel
)
from repository.medical_record import MedicalRecordRepo
from fastapi import HTTPException, status


class MedicalRecordService(IService):
    def __init__(self, db, user):
        super().__init__(db, user)
        self._medical_record_repo = MedicalRecordRepo(db)

    @Permission.permit([UserRole.EMPLOYEE, UserRole.ADMIN])
    async def get(
        self,
        query: QueryMedicalRecordModel
    ) -> dict:
        medical_record, err = await self._medical_record_repo.get(query)
        if err:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Medical record not found"
            )
        return MedicalRecordModel.model_validate({
            c.name: str(getattr(medical_record, c.name)) for c in medical_record.__table__.columns
        }).model_dump()

    @Permission.permit([UserRole.PATIENT])
    async def get_me(self) -> dict:
        medical_record, err = await self._medical_record_repo.get(
            QueryMedicalRecordModel(patient_id=self._current_user["sub"])
        )
        if err:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Medical record not found"
            )
        return MedicalRecordModel.model_validate({
            c.name: str(getattr(medical_record, c.name)) for c in medical_record.__table__.columns
        }).model_dump()

    @Permission.permit([UserRole.EMPLOYEE, UserRole.ADMIN])
    async def create(
        self,
        medical_record: NewMedicalRecordModel
    ) -> dict:
        medical_record, err = await self._medical_record_repo.create(medical_record)
        if err:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Existing medical record"
            )
        return MedicalRecordModel.model_validate({
            c.name: str(getattr(medical_record, c.name)) for c in medical_record.__table__.columns
        }).model_dump()

    @Permission.permit([UserRole.EMPLOYEE, UserRole.ADMIN])
    async def delete(
        self,
        query: QueryMedicalRecordModel
    ) -> dict:
        medical_record, err = await self._medical_record_repo.delete(query)
        if medical_record is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Medical record not found")
        return MedicalRecordModel.model_validate({
            c.name: str(getattr(medical_record, c.name)) for c in medical_record.__table__.columns
        }).model_dump()

    @Permission.permit([UserRole.PATIENT, UserRole.EMPLOYEE, UserRole.ADMIN])
    async def update(
        self,
        query: QueryMedicalRecordModel,
        medical_record: PatchMedicalRecordModel
    ) -> dict:
        medical_record, err = await self._medical_record_repo.update(
            query, medical_record
        )
        if err:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Medical record not found")
        return MedicalRecordModel.model_validate({
            c.name: str(getattr(medical_record, c.name)) for c in medical_record.__table__.columns
        }).model_dump()
