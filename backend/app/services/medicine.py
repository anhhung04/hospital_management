from uuid import uuid4
from fastapi import HTTPException, Depends, status
from middleware.user_ctx import UserContext
from repository.user import UserRepo
from middleware.user_ctx import UserContext
from repository.warehouse import MedicineRepo
from permissions import Permission
from permissions.user import UserRole, EmployeeType
from util.log import logger
from models.medicine import(
  MedicineModel,
  MedicineRequestModel,
  AddMedicineModel,
  BatchModel,
  BatchRequestModel,
  AddBatchModel,
)

class MedicineService:
    def __init__(
        self,
        user: UserContext=Depends(UserContext),
        medicine_repo: MedicineRepo=Depends(MedicineRepo),
        user_repo: UserRepo=Depends(UserRepo),
    ):
        self._user = user
        self._medicine_repo = medicine_repo
        self._user_repo = user_repo
    
    # @Permission.permit([EmployeeType.MANAGER], acl=[UserRole.EMPLOYEE])
    async def list_medicines(self, page: int, medicine_per_page: int):
        page = 1 if page < 1 else page
        medicine_per_page = 1 if medicine_per_page <= 0 else medicine_per_page
        medicines, error = await self._medicine_repo.list_medicines(page, medicine_per_page)
        if error:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                                detail="Error in fetching medicines list")
        try:
            medicines = [MedicineModel(
                id=medicine.id,
                name=medicine.name,
                description=medicine.description,
                quantity=medicine.quantity
            ).model_dump() for medicine in medicines]
        except Exception as e:
            logger.error("Error in fetching medicines list", reason=e)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                                detail="Error in fetching medicines list")
        return medicines

    # @Permission.permit([EmployeeType.OTHER], acl=[UserRole.EMPLOYEE])
    async def get(self, id: str):
        medicine, error = await self._medicine_repo.get(id)
        if error:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                                detail="Error in fetching medicine")
        return MedicineModel(
            id=medicine.id,
            name=medicine.name,
            description=medicine.description,
            quantity=medicine.quantity
        ).model_dump()
    
    # @Permission.permit([EmployeeType.OTHER], acl=[UserRole.EMPLOYEE])
    async def create(self, medicine: MedicineRequestModel):
        print("test")
        medicine_info = medicine.model_dump()
        medicine_id = str(uuid4())
        medicine_info.update({"id": medicine_id})
        medicine, error = await self._medicine_repo.create(
            AddMedicineModel.model_validate(medicine_info)
        )
        if error:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                                detail="Error in creating medicine")
        return MedicineModel(
            id=medicine.id,
            name=medicine.name,
            description=medicine.description,
            quantity=medicine.quantity
        ).model_dump()
    
    # @Permission.permit([EmployeeType.OTHER], acl=[UserRole.EMPLOYEE])
    async def list_batches(self, medicine_id: str, page: int, batches_per_page: int):
        page = 1 if page < 1 else page
        batches_per_page = 1 if batches_per_page <= 0 else batches_per_page
        batches, error = await self._medicine_repo.get_batches(
            medicine_id=medicine_id,
            page=page,
            batches_per_page=batches_per_page
        )
        if error:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                                detail="Error in fetching medicine")
        try:
            batches = [BatchModel(
                id=batch.id,
                import_date=str(batch.import_date),
                quantity=batch.import_quantity,
                expiration_date=str(batch.expiration_date),
                price=batch.container_price,
                price_per_unit=batch.price_per_unit,
                manufacturer=batch.manufacturer,
                details=batch.details
            ).model_dump() for batch in batches]
        except Exception as e:
            logger.error("Error in fetching medicine batches", reason=e)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                                detail="Error in fetching medicine batches")
        return batches
    
    # @Permission.permit([EmployeeType.OTHER], acl=[UserRole.EMPLOYEE])
    async def create_batch(self, medicine_id: str, batch: BatchRequestModel):
        batch_info = batch.model_dump()
        batch_id = str(uuid4())
        batch_info.update({"id": batch_id})
        batch_info.update({"price_per_unit": batch_info.get("price") / batch_info.get("quantity")})
        batch, error = await self._medicine_repo.create_batch(
            medicine_id,
            AddBatchModel.model_validate(batch_info)
        )
        if error:
            print(error)
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                                detail="Error in adding batch")
        return BatchModel(
            id=batch.id,
            quantity=batch.import_quantity,
            expiration_date=str(batch.expiration_date),
            import_date=str(batch.import_date),
            price=batch.container_price,
            price_per_unit=batch.price_per_unit,
            manufacturer=batch.manufacturer,
            details=batch.details
        ).model_dump()
    
    # @Permission.permit([EmployeeType.OTHER], acl=[UserRole.EMPLOYEE])
    async def get_batch(self, medicine_id: str, batch_id: str):
        batch, error = await self._medicine_repo.get_batch(medicine_id, batch_id)
        if error:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
                                detail="Error in fetching batch")
        if not batch:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail="Batch not found")
        return BatchModel(
            id=batch.id,
            quantity=batch.import_quantity,
            expiration_date=str(batch.expiration_date),
            import_date=str(batch.import_date),
            price=batch.container_price,
            price_per_unit=batch.price_per_unit,
            manufacturer=batch.manufacturer,
            details=batch.details
        ).model_dump()