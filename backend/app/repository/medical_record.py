from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from repository.schemas.patient import MedicalRecord
from models.medical_record import NewMedicalRecordModel, QueryMedicalRecordModel, PatchMedicalRecordModel
from models.medical_record import MedicalRecord
from typing import Tuple, Optional

class MedicalRecordRepo:
    def __init__(self, db: Session):
        self.__sess = db

    async def get(
        self,
        patient_id: str
    ) -> Tuple[MedicalRecord, Exception]:
        try:
            return self.__sess.query(MedicalRecord).filter(MedicalRecord.patient_id == patient_id).first(), None
        except Exception as err:
            return None, err

    async def create(
        self,
        medical_record: NewMedicalRecordModel
    ) -> Tuple[MedicalRecord, Optional[Exception | IntegrityError]]:
        try:
            new_medical_record = MedicalRecord(**medical_record.model_dump())
            self.__sess.add(new_medical_record)
            self.__sess.commit()
        except IntegrityError as err:
            return None, err
        except Exception as err:
            return None, err
        return new_medical_record, None

    async def delete(
        self,
        query: QueryMedicalRecordModel
    ) -> Tuple[MedicalRecord, Exception]:
        try:
            medical_record = self.__sess.query(MedicalRecord).filter(
                MedicalRecord.id == query.id or MedicalRecord.patient_id == query.patient_id
            ).first()
            self.__sess.delete(medical_record)
            self.__sess.commit()
        except Exception as err:
            return None, err
        return medical_record, None

    async def update(
        self,
        query: QueryMedicalRecordModel,
        update_medical_record: PatchMedicalRecordModel
    ) -> Tuple[MedicalRecord, Exception]:
        try:
            medical_record = self.__sess.query(MedicalRecord).filter(
                MedicalRecord.id == query.id or MedicalRecord.patient_id == query.patient_id
            ).first()
            for attr in update_medical_record.keys():
                setattr(medical_record, attr, update_medical_record.get(attr))
            self.__sess.add(medical_record)
            self.__sess.commit()
            self.__sess.refresh(medical_record)
        except Exception as err:
            return None, err
        return medical_record, None
