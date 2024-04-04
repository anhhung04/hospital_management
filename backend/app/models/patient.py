from pydantic import BaseModel
from models.response import BaseResponseModel
from models.user import PatchUserDetailModel, UserDetailResponse
from typing import Optional


class PatientModel(BaseModel):
    id: str
    full_name: str
    phone_number: str
    appointment_date: Optional[str] = None
    medical_record: Optional[int] = None


class PatientResponseModel(BaseResponseModel):
    data: PatientModel

class ListPatientsModel(BaseResponseModel):
    data: list[PatientModel]


class AddPatientModel(BaseModel):
    patient_id: str

class AddPatientResponseModel(BaseResponseModel):
    data: PatientResponseModel

class NewPatientModel(BaseModel):
    username: str
    password: str
    user_id: str


class NewPatientReponseModel(BaseResponseModel):
    data: NewPatientModel


class PatientDetailModel(BaseModel):
    appointment_date: Optional[str] = None
    medical_record: Optional[int] = None
    personal_info: UserDetailResponse


class PatientDetailResponseModel(BaseResponseModel):
    data: PatientDetailModel


class PatchPatientModel(PatchUserDetailModel):
    pass


class QueryPatientModel(BaseModel):
    user_id: Optional[str] = None
