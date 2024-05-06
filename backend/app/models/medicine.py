from pydantic import BaseModel, Field
from models.response import BaseResponseModel
from typing import Optional

class MedicineModel(BaseModel):
    id: str
    name: str
    description: str
    quantity: int = Field(ge=0)

class MedicineListResponseModel(BaseResponseModel):
    data: list[MedicineModel]

class MedicineRequestModel(BaseModel):
    name: str
    description: str
    quantity: int = Field(ge=0, default=0)

class AddMedicineModel(MedicineRequestModel):
    id: str

class BatchModel(BaseModel):
    id: str
    import_date: str
    expiration_date: str
    quantity: int = Field(gt=0)
    price: float = Field(gt=0)
    price_per_unit: float = Field(gt=0)
    manufacturer: str
    details: str

class BatchRequestModel(BaseModel):
    import_date: str
    expiration_date: str
    quantity: int = Field(gt=0)
    price: float = Field(gt=0)
    price_per_unit: Optional[float] = Field(default=None, gt=0)
    manufacturer: str
    details: str

class AddBatchModel(BatchRequestModel):
    id: str

class BatchListResponseModel(BaseResponseModel):
    data: list[BatchModel]