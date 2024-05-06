from fastapi import Depends
from repository import Storage
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from repository.user import UserRepo
from repository.schemas.user import User
from models.medicine import(
  AddMedicineModel,
  AddBatchModel,
)
from repository.schemas.warehouse import(
  Medicine,
  MedicineBatch,
  ContainerType
)
from typing import Tuple


class MedicineRepo:
    def __init__(
        self,
        user_repo: UserRepo=Depends(UserRepo),
        session: Session = Depends(Storage.get)
    ):
        self._sess = session
        self._user_repo = user_repo

    async def list_medicines(self, page: int, medicine_per_page: int) -> Tuple[list[Medicine], Exception | None]:
        try:
            query = self._sess.query(Medicine)
            query = query.limit(medicine_per_page).offset(
                (page - 1) * medicine_per_page
            )
            medicines = query.all()
        except Exception as e:
            return [], e
        return medicines, None
    
    async def get(self, id: str) -> Tuple[Medicine, Exception | None]:
        try:
            medicine = self._sess.query(Medicine).filter(
                Medicine.id == id).first()
        except Exception as e:
            return None, e
        return medicine, None
    
    async def create(self, medicine: AddMedicineModel) -> Tuple[Medicine, Exception | None]:
        try:
            new_medicine = Medicine(
                id=medicine.id,
                name=medicine.name,
                description=medicine.description,
                quantity=medicine.quantity
            )
            self._sess.add(new_medicine)
            self._sess.commit()
        except IntegrityError as e:
            self._sess.rollback()
            return None, e
        except Exception as e:
            return None, e
        return new_medicine, None
    
    async def get_batches(self, medicine_id: str, page: int, batches_per_page: int) -> Tuple[list[MedicineBatch], Exception | None]:
        try:
            query = self._sess.query(MedicineBatch).filter(
                MedicineBatch.medicine_id == medicine_id
            )
            query = query.limit(batches_per_page).offset(
                (page - 1) * batches_per_page
            )
            batches = query.all()
        except Exception as e:
            return [], e
        return batches, None
    
    async def get_batch(self, medicine_id: str, batch_id: str) -> Tuple[MedicineBatch, Exception | None]:
        try:
            batch = self._sess.query(MedicineBatch).filter(
                MedicineBatch.id == batch_id
            ).first()
        except Exception as e:
            return None, e
        if batch.medicine_id != medicine_id:
            return None, Exception("Batch does not belong to the medicine")
        return batch, None
    
    async def create_batch(self, medicine_id: str, batch: AddBatchModel) -> Tuple[MedicineBatch, Exception | None]:
        try:
            new_batch = MedicineBatch(
                id=batch.id,
                medicine_id=medicine_id,
                import_date=batch.import_date,
                expiration_date=batch.expiration_date,
                import_quantity=batch.quantity,
                details=batch.details,
                container_price=batch.price,
                price_per_unit=batch.price_per_unit,
                manufacturer=batch.manufacturer,
                container_type=ContainerType.MEDICINE
            )
            self._sess.add(new_batch)
            self._sess.commit()
        except IntegrityError as e:
            self._sess.rollback()
            return None, e
        except Exception as e:
            return None, e
        return new_batch, None
    

    

        