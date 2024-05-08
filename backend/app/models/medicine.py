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

class MedicineBatchModel(BaseModel):
    id: str
    import_date: str
    expiration_date: str
    quantity: int = Field(gt=0)
    price: float = Field(gt=0)
    price_per_unit: float = Field(gt=0)
    manufacturer: str
    details: str

class MedicineBatchRequestModel(BaseModel):
    import_date: str
    expiration_date: str
    quantity: int = Field(gt=0)
    price: float = Field(gt=0)
    price_per_unit: Optional[float] = Field(default=None, gt=0)
    manufacturer: str
    details: str

class AddMedicineBatchModel(MedicineBatchRequestModel):
    id: str

class MedicineBatchListResponseModel(BaseResponseModel):
    data: list[MedicineBatchModel]