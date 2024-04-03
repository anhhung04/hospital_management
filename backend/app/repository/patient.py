from collections import namedtuple
from repository.schemas.patient import Patient
from repository.user import UserRepo
from repository.schemas.user import User
from typing import Tuple


GetPatientQuery = namedtuple("GetPatientQuery", ["id", "username"])


class PatientRepo:
    def __init__(self, session):
        self._sess = session
        self._user_repo = UserRepo(session)

    async def get(self, patient_id: str) -> User:
        try:
            patient = self._sess.query(Patient).filter(
                Patient.user_id == patient_id).first()
        except Exception:
            return None
        return patient

    async def create(self, patient_info: dict) -> Tuple[Patient]:
        new_patient = Patient(**patient_info)
        try:
            self._sess.add(new_patient)
            self._sess.commit()
        except Exception:
            return None
        return new_patient

    async def update(self, query: GetPatientQuery, patient_update: dict) -> Tuple[Patient, str]:
        try:
            patient = self._sess.query(Patient).filter(
                Patient.user_id == query['user_id']).first()
            if not patient:
                return None
            for attr in patient_update.keys():
                setattr(patient, attr, patient_update[attr])
            self._sess.add(patient)
            self._sess.commit()
            self._sess.refresh(patient)
        except Exception as e:
            return None, e
        return patient, None

    async def list_patient(self, page: int, patient_per_page: int) -> list[Patient]:
        try:
            patients = self._sess.query(Patient).limit(
                patient_per_page).offset((page - 1) * patient_per_page).all()
        except Exception:
            return []
        return patients
