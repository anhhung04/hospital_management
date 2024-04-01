from sqlalchemy.orm import Session
from repository.patient import PatientRepo


class PatientService:
    def __init__(self, session: Session):
        self._repo = PatientRepo(session)

    def get_patients(self, page: int, patient_per_page: int):
        if page < 1:
            page = 1
        if patient_per_page < 1:
            patient_per_page = 10
        return self._repo.list_patient(page=1, patient_per_page=10)
