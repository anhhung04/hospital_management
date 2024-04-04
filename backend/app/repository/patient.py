from repository.schemas.patient import Patient
from repository.user import UserRepo
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import Tuple
from models.patient import QueryPatientModel, PatchPatientModel, AddPatientModel

class PatientRepo:
    def __init__(self, session: Session):
        self._sess = session
        self._user_repo = UserRepo(session)

    async def get(self, query: QueryPatientModel) -> Tuple[Patient, Exception]:
        try:
            patient = self._sess.query(Patient).filter(
                Patient.user_id == query.user_id
            ).first()
        except Exception as err:
            return None, err
        return patient, None

    async def create(self, patient_info: AddPatientModel) -> Tuple[Patient]:
        try:
            new_patient = Patient(**patient_info.model_dump_json())
            self._sess.add(new_patient)
            self._sess.commit()
        except IntegrityError as err:
            return None, err
        except Exception as err:
            return None, err
        return new_patient, None

    async def update(
        self,
        query: QueryPatientModel,
        patient_update: PatchPatientModel
    ) -> Tuple[Patient, Exception]:
        try:
            patient = self._sess.query(Patient).filter(
                Patient.user_id == query.user_id
            ).first()
            for attr in patient_update.keys():
                if patient_update.get(attr) is not None:
                    setattr(patient, attr, patient_update.get(attr))
            self._sess.add(patient)
            self._sess.commit()
            self._sess.refresh(patient)
        except Exception as err:
            return None, err
        return patient, None

    async def list_patient(
        self,
        page: int,
        limit: int
    ) -> Tuple[list[Patient], Exception]:
        try:
            patients = self._sess.query(Patient).limit(
                limit
            ).offset(
                (page - 1) * limit
            ).all()
        except Exception as err:
            return [], err
        return patients, None
