from repository import IRepo
from collections import namedtuple
from repository.schemas.patient import Patient
from repository.user import UserRepo
from repository.schemas.user import User
from util.crypto import PasswordContext
from permissions.user import UserRole
from permissions import Permission


GetPatientQuery = namedtuple("GetPatientQuery", ["id", "username"])


class PatientRepo(IRepo):
    def __init__(self, session):
        self._sess = session
        self._user_repo = UserRepo(session)

    def get(self, patient_id: str):
        try:
            patient = self._sess.query(Patient).filter(
                Patient.user_id == patient_id).first()
        except Exception:
            return None
        return patient

    def create(self, patient_info: dict):
        gen_password = PasswordContext.rand_key()
        username = f"patient_{patient_info['ssn']}"
        new_user = self._user_repo.create(User(
            id=patient_info['user_id'],
            ssn=patient_info['ssn'],
            phone_number=patient_info['phone_number'],
            birth_date=patient_info['birth_date'],
            gender=patient_info['gender'],
            health_insurance=patient_info['health_insurance'],
            last_name=patient_info['last_name'],
            first_name=patient_info['first_name'],
            address=patient_info['address'],
            email=patient_info['email'],
            role=Permission(str(UserRole.PATIENT)).get(),
            username=username,
            password=PasswordContext(gen_password, username).hash()
        ))
        user_in_db = self._user_repo.create(new_user)
        new_patient = Patient(
            user_id=user_in_db.id,
            weight=0,
            height=0,
        )
        self._sess.add(new_patient)
        self._sess.commit()
        return new_user, new_patient

    def update(self, query: GetPatientQuery, patient_update: dict):
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
