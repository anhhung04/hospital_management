from repository import IRepo
from collections import namedtuple
from repository.schemas.patient import Patient

GetPatientQuery = namedtuple("GetPatientQuery", ["id", "name"])


class PatientRepo(IRepo):
    def __init__(self, session):
        self._sess = session

    def get(self, patient_id: str):
        try:
            patient = self._sess.query(Patient).filter(
                Patient.user_id == patient_id).first()
        except Exception:
            return None
        return patient

    def list_patient(self, page: int, patient_per_page: int):
        try:
            patients = self._sess.query(Patient).limit(
                patient_per_page).offset((page - 1) * patient_per_page).all()
        except Exception:
            return []
        return patients
