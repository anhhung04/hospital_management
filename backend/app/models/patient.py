from pydantic import BaseModel
from models.response import BaseResponseModel

class PatientResponseModel(BaseModel):
    id: str
    full_name: str
    phone_number: str
    medical_record: str

class ListPatientsModel(BaseResponseModel):
    data: list[PatientResponseModel]
