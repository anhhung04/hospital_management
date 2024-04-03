from pydantic import BaseModel
from models.response import BaseResponseModel
from models.user import UserDetail
from typing import Optional


class PatientModel(BaseModel):
    id: str
    full_name: str
    phone_number: str
    medical_record: str


class PatientResponseModel(BaseResponseModel):
    data: PatientModel

class ListPatientsModel(BaseResponseModel):
    data: list[PatientModel]


class AddPatientRequestModel(BaseModel):
    first_name: str
    last_name: str
    birth_date: str
    gender: str
    ssn: str
    phone_number: str
    address: str
    email: str
    health_insurance: str
    
class AddPatientResponseModel(BaseResponseModel):
    data: PatientResponseModel


class NewPatientModel(BaseModel):
    username: str
    password: str
    user_id: str


class NewPatientReponseModel(BaseResponseModel):
    data: NewPatientModel


class PatientDetailModel(UserDetail):
    weight: float
    height: float
    note: str
    medical_record: int


class PatientDetailResponseModel(BaseResponseModel):
    data: PatientDetailModel


class NewPatientRequestModel(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    birth_date: Optional[str]
    gender: Optional[str]
    phone_number: Optional[str]
    address: Optional[str]
    email: Optional[str]
    health_insurance: Optional[str]
    weight: Optional[float]
    height: Optional[float]
