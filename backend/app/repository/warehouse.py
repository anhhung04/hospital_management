from fastapi import Depends
from repository import Storage
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from repository.user import UserRepo
from models.medicine import(
  AddMedicineModel,
  AddMedicineBatchModel,
)
from models.equipment import(
  AddEquipmentModel,
  AddEquipmentBatchModel,
)
from repository.schemas.warehouse import(
  Medicine,
  MedicineBatch,
  ContainerType,
  Equipment,
  EquipmentBatch,
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
    
    async def create_batch(self, medicine_id: str, batch: AddMedicineBatchModel) -> Tuple[MedicineBatch, Exception | None]:
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
            medicine = self._sess.query(Medicine).filter(
                Medicine.id == medicine_id
            ).first()
            medicine.quantity += new_batch.import_quantity
            self._sess.add(medicine)
            self._sess.commit()
        except IntegrityError as e:
            self._sess.rollback()
            return None, e
        except Exception as e:
            return None, e
        return new_batch, None
    

class EquipmentRepo():
    def __init__(
        self,
        user_repo: UserRepo=Depends(UserRepo),
        session: Session = Depends(Storage.get)
    ):
        self._sess = session
        self._user_repo = user_repo
    
    async def list_equipments(self, page: int, equipment_per_page: int) -> Tuple[list[Equipment], Exception | None]:
        try:
            query = self._sess.query(Equipment)
            query = query.limit(equipment_per_page).offset(
                (page - 1) * equipment_per_page
            )
            equipments = query.all()
        except Exception as e:
            return [], e
        return equipments, None
    
    async def get(self, id: str) -> Tuple[Equipment, Exception | None]:
        try:
            equipment = self._sess.query(Equipment).filter(
                Equipment.id == id).first()
        except Exception as e:
            return None, e
        return equipment, None
    
    async def create(self, equipment: AddEquipmentModel) -> Tuple[Equipment, Exception | None]:
        try:
            new_equipment = Equipment(
                id=equipment.id,
                name=equipment.name,
                description=equipment.description,
                availability=equipment.availability,
                status=equipment.status,
                maintanance_history=equipment.maintanance_history,
                quantity=equipment.quantity
            )
            self._sess.add(new_equipment)
            self._sess.commit()
        except IntegrityError as e:
            self._sess.rollback()
            return None, e
        except Exception as e:
            return None, e
        return new_equipment, None
    
    async def get_batches(self, equipment_id: str, page: int, batches_per_page: int) -> Tuple[list[EquipmentBatch], Exception | None]:
        try:
            query = self._sess.query(EquipmentBatch).filter(
                EquipmentBatch.equipment_id == equipment_id
            )
            query = query.limit(batches_per_page).offset(
                (page - 1) * batches_per_page
            )
            batches = query.all()
        except Exception as e:
            return [], e
        return batches, None
    
    async def get_batch(self, equipment_id: str, batch_id: str) -> Tuple[EquipmentBatch, Exception | None]:
        try:
            batch = self._sess.query(EquipmentBatch).filter(
                EquipmentBatch.id == batch_id
            ).first()
        except Exception as e:
            return None, e
        if batch.equipment_id != equipment_id:
            return None, Exception("Batch does not belong to the equipment")
        return batch, None
    
    async def create_batch(self, equipment_id: str, batch: AddEquipmentBatchModel) -> Tuple[EquipmentBatch, Exception | None]:
        try:
            new_batch = EquipmentBatch(
                id=batch.id,
                equipment_id=equipment_id,
                import_date=batch.import_date,
                import_quantity=batch.import_quantity,
                details=batch.details,
                container_price=batch.container_price,
                price_per_unit=batch.price_per_unit,
                container_type=ContainerType.EQUIPMENT,
                manufacturer=batch.manufacturer
            )
            self._sess.add(new_batch)
            self._sess.commit()
            equipment = self._sess.query(Equipment).filter(
                Equipment.id == equipment_id
            ).first()
            equipment.quantity += new_batch.import_quantity
            self._sess.add(equipment)
            self._sess.commit()
        except IntegrityError as e:
            self._sess.rollback()
            return None, e
        except Exception as e:
            return None, e
        return new_batch, None
    
            

    