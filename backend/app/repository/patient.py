from repository import IRepo
from collections import namedtuple
from repository.schemas.patient import Patient
from util.log import logger

GetPatientQuery = namedtuple("GetPatientQuery", ["id", "name"])


class PatientRepo(IRepo):
    def __init__(self, session):
        self._sess = session

    def list_patient(self, page: int, patient_per_page: int):
        try:
            patients = self._sess.query(Patient).limit(
                patient_per_page).offset((page - 1) * patient_per_page).all()
        except Exception as e:
            logger.error('Error in listing patients', reason=e)
            return []
        return patients
