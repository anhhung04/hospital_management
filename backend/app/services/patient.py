from sqlalchemy.orm import Session
from repository.patient import PatientRepo
from services import IService
from util.log import logger
from fastapi import HTTPException
from models.patient import PatientResponseModel
from permissions import Permission
from permissions.user import UserRole
class PatientService(IService):
    def __init__(self, session: Session, user: dict = None):
        super().__init__(session, user, None)
        self._repo = PatientRepo(session)

    @Permission.permit([UserRole.ADMIN, UserRole.EMPLOYEE])
    def get_patients(self, page: int = 1, patient_per_page: int = 10):
        if page < 1:
            page = 1
        if patient_per_page < 1:
            patient_per_page = 10
        patients = self._repo.list_patient(page, patient_per_page)
        try:
            patients = [PatientResponseModel(
                id=p.user_id,
                full_name=" ".join(
                    [p.personal_info.last_name, p.personal_info.first_name]),
                phone_number=p.personal_info.phone_number,
                medical_record=str(p.medical_record.id)
            ).model_dump() for p in patients]
        except Exception as e:
            logger.error('Error in convert patients list', reason=e)
            raise HTTPException(
                status_code=500, detail='Error in convert patients list')
        return patients

    @Permission.permit([UserRole.ADMIN, UserRole.EMPLOYEE, UserRole.PATIENT])
    def get(self, patient_id: str):
        if Permission.has_role([UserRole.PATIENT], self._current_user):
            if self._current_user['sub'] != patient_id:
                raise HTTPException(status_code=403, detail='Permission denied')
        patient = self._repo.get(patient_id)
        if not patient:
            raise HTTPException(status_code=404, detail='Patient not found')
        return PatientResponseModel(
            id=patient.user_id,
            full_name=" ".join(
                [patient.personal_info.last_name, patient.personal_info.first_name]),
            phone_number=patient.personal_info.phone_number,
            medical_record=str(patient.medical_record.id)
        ).model_dump()
