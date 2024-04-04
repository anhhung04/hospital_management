from sqlalchemy.orm import Session
from repository.patient import PatientRepo
from services import IService
from fastapi import HTTPException, status
from models.patient import PatientModel, PatientDetailModel, NewPatientModel
from permissions import Permission
from permissions.user import UserRole
from repository.patient import GetPatientQuery
from repository.user import UserRepo
from repository.schemas.patient import Patient, ProgressType
from util.crypto import PasswordContext

class PatientService(IService):
    def __init__(self, session: Session, user: dict = None):
        super().__init__(session, user, None)
        self._patient_repo = PatientRepo(session)
        self._user_repo = UserRepo(session)

    @Permission.permit([UserRole.ADMIN, UserRole.EMPLOYEE])
    async def get_patients(self, page: int = 1, patient_per_page: int = 10):
        if page < 1:
            page = 1
        if patient_per_page < 1:
            patient_per_page = 10
        patients = await self._patient_repo.list_patient(page, patient_per_page)

        def process_patient(patient: Patient):
            appointment_date = None
            progress = patient.medical_record.progress if patient.medical_record else None
            if progress:
                latest_progress = progress.sort(
                    lambda x: x.created_at, reverse=True
                )[0]
                appointment_date = latest_progress.created_at if latest_progress.status == ProgressType.SCHEDULING else None
            return PatientModel(
                id=patient.user_id,
                full_name=f"{patient.personal_info.first_name} {
                    patient.personal_info.last_name}",
                phone_number=patient.personal_info.phone_number,
                medical_record=patient.medical_record.id if patient.medical_record else None,
                appointment_date=str(appointment_date),
            ).model_dump()
        try:
            patients = [process_patient(p) for p in patients]
        except Exception:
            raise HTTPException(
                status_code=500, detail='Error in convert patients list')
        return patients

    @Permission.permit([UserRole.ADMIN, UserRole.EMPLOYEE])
    async def get(self, patient_id: str):
        if Permission.has_role([UserRole.PATIENT], self._current_user):
            if self._current_user['sub'] != patient_id:
                raise HTTPException(status_code=403, detail='Permission denied')
        patient = await self._patient_repo.get(patient_id)
        if not patient:
            raise HTTPException(status_code=404, detail='Patient not found')
        return PatientDetailModel(
            id=patient.user_id,
            ssn=patient.personal_info.ssn,
            phone_number=patient.personal_info.phone_number,
            address=patient.personal_info.address,
            email=patient.personal_info.email,
            health_insurance=patient.personal_info.health_insurance,
            weight=patient.weight,
            height=patient.height,
            note=patient.note,
            username=patient.personal_info.username,
            role=patient.personal_info.role,
            first_name=patient.personal_info.first_name,
            last_name=patient.personal_info.last_name,
            birth_date=str(patient.personal_info.birth_date),
            medical_record=patient.medical_record.id if patient.medical_record else None,
            gender=patient.personal_info.gender
        ).model_dump()

    @Permission.permit([UserRole.EMPLOYEE])
    async def create(self, user_info: dict):
        raw_password = PasswordContext.rand_key()
        user_info.update({
            "password": PasswordContext(raw_password, user_info['username']).hash(),
            "username": f"patient_{user_info['ssn']}",
            "role": Permission(UserRole.PATIENT).get(),
        })
        user_in_db = await self._user_repo.create(user_info)
        if not user_in_db:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='User is already existed')
        patient_info = {
            "user_id": user_in_db.id,
        }
        patient_in_db = await self._patient_repo.create(patient_info)
        if not patient_in_db:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Error in create patient')
        return NewPatientModel.model_validate({
            c.name: str(getattr(patient_in_db, c.name)) for c in patient_in_db.__table__.columns
        }).model_dump()

    @Permission.permit([UserRole.ADMIN, UserRole.EMPLOYEE])
    async def update(self, user_id: str, patient_update: dict):
        patient, err = await self._patient_repo.update(query=GetPatientQuery(
            user_id, None), patient_update=patient_update)
        if err:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Error in update patient infomation')
        return PatientDetailModel(
            id=patient.user_id,
            ssn=patient.personal_info.ssn,
            phone_number=patient.personal_info.phone_number,
            address=patient.personal_info.address,
            email=patient.personal_info.email,
            health_insurance=patient.personal_info.health_insurance,
            weight=patient.weight,
            height=patient.height,
            note=patient.note,
            username=patient.personal_info.username,
            role=patient.personal_info.role,
            first_name=patient.personal_info.first_name,
            last_name=patient.personal_info.last_name,
            birth_date=patient.personal_info.birth_date,
            medical_record=patient.medical_record.medical_record,
        ).model_dump()
