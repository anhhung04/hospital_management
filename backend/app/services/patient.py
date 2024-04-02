from sqlalchemy.orm import Session
from repository.patient import PatientRepo
from models.patient import PatientResponseMode

class PatientService:
    def __init__(self, session: Session):
        self._repo = PatientRepo(session)

    def get_patients(self, page: int = 1, patient_per_page: int = 10):
        if page < 1:
            page = 1
        if patient_per_page < 1:
            patient_per_page = 10
        patients = self._repo.list_patient(page=page, patient_per_page=patient_per_page)
        
