from pydantic import BaseModel, Field
from models.response import BaseResponseModel


class EquipmentModel(BaseModel):
    id: str
    name: str
    availability: bool
    maintanance_history: str
    description: str
    status: str
    quantity: int = Field(ge=0)

class EquipmentListResponseModel(BaseResponseModel):
    data: list[EquipmentModel]

class EquipmentRequestModel(BaseModel):
    name: str = Field(min_length=1)
    availability: bool
    maintanance_history: str = Field(min_length=1)
    description: str = Field(min_length=1)
    status: str = Field(min_length=1)
    quantity: int = Field(ge=0, default=0)

class AddEquipmentModel(EquipmentRequestModel):
    id: str

class EquipmentBatchModel(BaseModel):
    id: str
    import_date: str
    import_quantity: int = Field(gt=0)
    container_price: float = Field(gt=0)
    price_per_unit: float = Field(gt=0)
    manufacturer: str
    details: str

class EquipmentBatchRequestModel(BaseModel):
    import_date: str
    import_quantity: int = Field(gt=0)
    container_price: float = Field(gt=0)
    price_per_unit: float = Field(gt=0)
    manufacturer: str = Field(min_length=1)
    details: str = Field(min_length=1)

class AddEquipmentBatchModel(EquipmentBatchRequestModel):
    id: str

class EquipmentBatchListResponseModel(BaseResponseModel):
    data: list[EquipmentBatchModel]


