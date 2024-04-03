from sqlalchemy.orm import Session
from repository.patient import PatientRepo
from services import IService
from util.log import logger
from fastapi import HTTPException, status
from models.patient import PatientModel, PatientDetailModel, NewPatientModel
from permissions import Permission
from permissions.user import UserRole
from repository.patient import GetPatientQuery

class PatientService(IService):
    def __init__(self, session: Session, user: dict = None):
        super().__init__(session, user, None)
        self._patient_repo = PatientRepo(session)

    @Permission.permit([UserRole.ADMIN, UserRole.EMPLOYEE])
    async def get_patients(self, page: int = 1, patient_per_page: int = 10):
        if page < 1:
            page = 1
        if patient_per_page < 1:
            patient_per_page = 10
        patients = await self._patient_repo.list_patient(page, patient_per_page)
        try:
            patients = [PatientModel(
                id=p.user_id,
                full_name=" ".join(
                    [p.personal_info.last_name, p.personal_info.first_name]),
                phone_number=p.personal_info.phone_number,
                medical_record=str(
                    p.medical_record.id) if p.medical_record else None,
            ).model_dump() for p in patients]
        except Exception as e:
            logger.error('Error in convert patients list', reason=e)
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
        new_user, _, raw_password = await self._patient_repo.create(user_info)
        if not new_user:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Existed patient')
        return NewPatientModel(
            username=new_user.username,
            password=raw_password,
            user_id=new_user.id
        ).model_dump()

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
