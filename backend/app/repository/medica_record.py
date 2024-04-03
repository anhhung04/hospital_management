from sqlalchemy.orm import Session
from repository.schemas.patient import MedicalRecord


class MedicalRecordRepo:
    def __init__(self, db: Session):
        self.__sess = db

    async def get(self, patient_id: str):
        try:
            return self.__sess.query(MedicalRecord).filter(MedicalRecord.patient_id == patient_id).first()
        except Exception:
            return None

    async def create(self, medical_record: dict):
        new_medical_record = MedicalRecord(**medical_record)
        self.__sess.add(new_medical_record)
        self.__sess.commit()
        return new_medical_record
