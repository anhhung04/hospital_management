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
        try:
            new_medical_record = MedicalRecord(**medical_record)
            self.__sess.add(new_medical_record)
            self.__sess.commit()
        except Exception:
            return None
        return new_medical_record

    async def delete(self, medical_record_id: str):
        medical_record = self.__sess.query(MedicalRecord).filter(
            MedicalRecord.id == medical_record_id).first()
        if medical_record is None:
            return None
        self.__sess.delete(medical_record)
        self.__sess.commit()
        return medical_record

    async def update(self, query: dict, update_medical_record: dict):
        medical_record = self.__sess.query(MedicalRecord).filter(
            MedicalRecord.patient_id == query.get('patient_id')).first()
        if medical_record is None:
            return None
        for attr in update_medical_record.keys():
            setattr(medical_record, attr, update_medical_record.get(attr))
        self.__sess.add(medical_record)
        self.__sess.commit()
        self.__sess.refresh(medical_record)
        return medical_record
