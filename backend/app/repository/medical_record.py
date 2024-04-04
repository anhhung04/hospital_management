from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from repository.schemas.patient import MedicalRecord
from models.medical_record import (
    NewMedicalRecordModel, QueryMedicalRecordModel, PatchMedicalRecordModel
)
from fastapi import Depends
from repository import Storage
from typing import Tuple, Optional

class MedicalRecordRepo:
    def __init__(self, db: Session = Depends(Storage.get)):
        self.__sess = db

    @staticmethod
    async def call():
        return MedicalRecordRepo()

    async def get(
        self,
        query: QueryMedicalRecordModel
    ) -> Tuple[MedicalRecord, Exception]:
        try:
            record = self.__sess.query(MedicalRecord).filter(
                MedicalRecord.patient_id == query.patient_id if query.patient_id else None
                or MedicalRecord.id == query.id if query.id else None
            ).first()
            if not record:
                return None, "Medical record not found"
            return record, None
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
            medical_record, err = await self.get(query)
            if err:
                return None, err
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
            medical_record, err = await self.get(query)
            if err:
                return None, err
            dump_medical_record = update_medical_record.model_dump()
            for attr in dump_medical_record.model_dump_json().keys():
                if dump_medical_record.get(attr) is not None:
                    setattr(
                        medical_record, attr,
                        dump_medical_record.get(attr)
                    )
            self.__sess.add(medical_record)
            self.__sess.commit()
            self.__sess.refresh(medical_record)
        except Exception as err:
            return None, err
        return medical_record, None
