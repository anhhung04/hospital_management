from uuid import uuid4
from fastapi import HTTPException, Depends, status
from middleware.user_ctx import UserContext
from repository.user import UserRepo
from middleware.user_ctx import UserContext
from repository.warehouse import EquipmentRepo
from permissions import Permission
from permissions.user import UserRole, EmployeeType
from util.log import logger
from models.equipment import(
  EquipmentModel,
  EquipmentRequestModel,
  AddEquipmentModel,
  EquipmentBatchModel,
  EquipmentBatchRequestModel,
  AddEquipmentBatchModel
)

class EquipmentService():
    def __init__(
        self,
        user_repo: UserRepo=Depends(UserRepo),
        user: UserContext=Depends(UserContext),
        equipment_repo: EquipmentRepo=Depends(EquipmentRepo)
    ):
        self._current_user = user
        self._user_repo = user_repo
        self._equipment_repo = equipment_repo

    @Permission.permit([EmployeeType.OTHER])
    async def list_equipments(self, page: int, equipment_per_page: int):
        page = 1 if page < 1 else page
        equipment_per_page = 1 if equipment_per_page <= 0 else equipment_per_page
        equipments, error = await self._equipment_repo.list_equipments(page, equipment_per_page)
        if error:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                                detail="Error in fetching equipments list")
        try:
            equipments = [EquipmentModel(
                id=equipment.id,
                name=equipment.name,
                description=equipment.description,
                maintanance_history=equipment.maintanance_history,
                status=equipment.status,
                availability=equipment.availability,
                quantity=equipment.quantity
            ).model_dump() for equipment in equipments]
        except Exception as e:
            logger.error("Error in fetching equipments list", reason=e)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                                detail="Error in fetching equipments list")
        return equipments
    
    @Permission.permit([EmployeeType.OTHER])
    async def get(self, id: str):
        equipment, error = await self._equipment_repo.get(id)
        if error:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                                detail="Error in fetching equipment")
        if not equipment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail="Equipment not found")
        return EquipmentModel(
            id=equipment.id,
            name=equipment.name,
            description=equipment.description,
            quantity=equipment.quantity,
            status=equipment.status,
            availability=equipment.availability,
            maintanance_history=equipment.maintanance_history
        ).model_dump()
    
    @Permission.permit([EmployeeType.OTHER])
    async def create(self, new_equipment_request: EquipmentRequestModel):
        new_equipment = AddEquipmentModel(
            id=str(uuid4()),
            name=new_equipment_request.name,
            description=new_equipment_request.description,
            quantity=new_equipment_request.quantity,
            status=new_equipment_request.status,
            availability=new_equipment_request.availability,
            maintanance_history=new_equipment_request.maintanance_history
        )
        equipment, error = await self._equipment_repo.create(new_equipment)
        if error:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                                detail="Error in creating equipment")
        return EquipmentModel(
            id=equipment.id,
            name=equipment.name,
            description=equipment.description,
            quantity=equipment.quantity,
            status=equipment.status,
            availability=equipment.availability,
            maintanance_history=equipment.maintanance_history
        ).model_dump()
    
    @Permission.permit([EmployeeType.OTHER])
    async def list_batches(self, equipment_id: str, page: int, batches_per_page: int):
        page = 1 if page < 1 else page
        batches_per_page = 1 if batches_per_page <= 0 else batches_per_page
        batches, error = await self._equipment_repo.get_batches(equipment_id, page, batches_per_page)
        if error:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                                detail="Error in fetching equipment batches")
        try:
            batches = [EquipmentBatchModel(
                id=batch.id,
                import_date=str(batch.import_date),
                import_quantity=batch.import_quantity,
                container_price=batch.container_price,
                price_per_unit=batch.price_per_unit,
                manufacturer=batch.manufacturer,
                details=batch.details
            ).model_dump() for batch in batches]
        except Exception as e:
            logger.error("Error in fetching equipment batches", reason=e)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                                detail="Error in fetching equipment batches")
        return batches
    
    @Permission.permit([EmployeeType.OTHER])
    async def get_batch(self, equipment_id: str, batch_id: str):
        batch, error = await self._equipment_repo.get_batch(equipment_id, batch_id)
        if error:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                                detail="Error in fetching equipment batch")
        if not batch:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail="Batch not found")
        return EquipmentBatchModel(
            id=batch.id,
            import_date=str(batch.import_date),
            import_quantity=batch.import_quantity,
            container_price=batch.container_price,
            price_per_unit=batch.price_per_unit,
            manufacturer=batch.manufacturer,
            details=batch.details
        ).model_dump()
    
    @Permission.permit([EmployeeType.OTHER])
    async def create_batch(self, equipment_id: str, batch: EquipmentBatchRequestModel):
        new_batch = AddEquipmentBatchModel(
            id=str(uuid4()),
            import_date=str(batch.import_date),
            import_quantity=batch.import_quantity,
            container_price=batch.container_price,
            price_per_unit=batch.price_per_unit,
            manufacturer=batch.manufacturer,
            details=batch.details
        )
        batch, error = await self._equipment_repo.create_batch(equipment_id, new_batch)
        if error:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                                detail="Error in creating equipment batch")
        return EquipmentBatchModel(
            id=batch.id,
            import_date=str(batch.import_date),
            import_quantity=batch.import_quantity,
            container_price=batch.container_price,
            price_per_unit=batch.price_per_unit,
            manufacturer=batch.manufacturer,
            details=batch.details
        ).model_dump()



