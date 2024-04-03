from services import IService
from permissions import Permission
from permissions.user import UserRole
from models.medical_record import MedicalRecordModel
from repository.medica_record import MedicalRecordRepo
from repository.schemas.patient import MedicalRecord
from fastapi import HTTPException


class MedicalRecordService(IService):
    def __init__(self, db, user):
        super().__init__(db, user)
        self._medical_record_repo = MedicalRecordRepo(db)

    @Permission.permit([UserRole.EMPLOYEE, UserRole.ADMIN])
    async def get(self, patient_id: str) -> MedicalRecordModel:
        medical_record: MedicalRecord = await self._medical_record_repo.get(patient_id)
        if medical_record is None:
            raise HTTPException(
                status_code=404, detail="Medical record not found")
        return MedicalRecordModel.model_validate({
            c.name: str(getattr(medical_record, c.name)) for c in medical_record.__table__.columns
        })

    @Permission.permit([UserRole.PATIENT])
    async def get_me(self) -> MedicalRecordModel:
        medical_record: MedicalRecord = await self._medical_record_repo.get(self._current_user.get('sub'))
        if medical_record is None:
            raise HTTPException(
                status_code=404, detail="Medical record not found")
        return MedicalRecordModel.model_validate({
            c.name: str(getattr(medical_record, c.name)) for c in medical_record.__table__.columns
        })

    @Permission.permit([UserRole.EMPLOYEE, UserRole.ADMIN])
    async def create(self, medical_record: dict) -> MedicalRecordModel:
        exist_medical_record: MedicalRecord = await self._medical_record_repo.get(medical_record.get('patient_id'))
        if exist_medical_record is not None:
            raise HTTPException(status_code=400, detail="Medical record already exist")
        medical_record: MedicalRecord = await self._medical_record_repo.create(medical_record)
        return MedicalRecordModel.model_validate({
            c.name: str(getattr(medical_record, c.name)) for c in medical_record.__table__.columns
        })

    @Permission.permit([UserRole.EMPLOYEE, UserRole.ADMIN])
    async def delete(self, medical_record_id: str) -> MedicalRecordModel:
        medical_record: MedicalRecord = await self._medical_record_repo.delete(medical_record_id)
        if medical_record is None:
            raise HTTPException(
                status_code=404, detail="Medical record not found")
        return MedicalRecordModel.model_validate({
            c.name: str(getattr(medical_record, c.name)) for c in medical_record.__table__.columns
        })
