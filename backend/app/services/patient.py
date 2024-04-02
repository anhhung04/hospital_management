from sqlalchemy.orm import Session
from repository.patient import PatientRepo
from models.patient import PatientResponseMode
from services import IService

class PatientService(IService):
    def __init__(self, session: Session, user: dict = None):
        self._repo = PatientRepo(session, None, user)
        
    def get_patients(self, page: int = 1, patient_per_page: int = 10) -> PatientResponseMode:
        if page < 1:
            page = 1
        if patient_per_page < 1:
            patient_per_page = 10
        patients = self._repo.list_patient(page=page, patient_per_page=patient_per_page)
        patients = list(map(
            lambda p: PatientResponseMode(
                id=p.user_id,
                full_name=" ".join([p.personal_info.last_name, p.personal_info.last_name]),
                phone_number=p.personal_info.phone_number,
                medical_record=p.medical_record.id
            ),
            patients
        ))
        return patients
