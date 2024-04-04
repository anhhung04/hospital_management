from services import IService
from permissions import Permission
from permissions.user import UserRole
from models.medical_record import MedicalRecordModel
from repository.medical_record import MedicalRecordRepo
from repository.schemas.patient import MedicalRecord
from fastapi import HTTPException, status


class MedicalRecordService(IService):
    def __init__(self, db, user):
        super().__init__(db, user)
        self._medical_record_repo = MedicalRecordRepo(db)

    @Permission.permit([UserRole.EMPLOYEE, UserRole.ADMIN])
    async def get(self, patient_id: str) -> MedicalRecordModel:
        medical_record: MedicalRecord = await self._medical_record_repo.get(patient_id)
        if medical_record is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Medical record not found")
        return MedicalRecordModel.model_validate({
            c.name: str(getattr(medical_record, c.name)) for c in medical_record.__table__.columns
        }).model_dump()

    @Permission.permit([UserRole.PATIENT])
    async def get_me(self) -> MedicalRecordModel:
        medical_record: MedicalRecord = await self._medical_record_repo.get(self._current_user.get('sub'))
        if medical_record is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Medical record not found")
        return MedicalRecordModel.model_validate({
            c.name: str(getattr(medical_record, c.name)) for c in medical_record.__table__.columns
        }).model_dump()

    @Permission.permit([UserRole.EMPLOYEE, UserRole.ADMIN])
    async def create(self, medical_record: dict) -> MedicalRecordModel:
        medical_record: MedicalRecord = await self._medical_record_repo.create(medical_record)
        if medical_record is None:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Existing medical record")
        return MedicalRecordModel.model_validate({
            c.name: str(getattr(medical_record, c.name)) for c in medical_record.__table__.columns
        }).model_dump()

    @Permission.permit([UserRole.EMPLOYEE, UserRole.ADMIN])
    async def delete(self, medical_record_id: str) -> MedicalRecordModel:
        medical_record: MedicalRecord = await self._medical_record_repo.delete(medical_record_id)
        if medical_record is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Medical record not found")
        return MedicalRecordModel.model_validate({
            c.name: str(getattr(medical_record, c.name)) for c in medical_record.__table__.columns
        }).model_dump()
