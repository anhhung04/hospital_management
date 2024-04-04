from pydantic import BaseModel
from models.response import BaseResponseModel
from models.user import UserDetail, PatchUserDetailModel, AddUserModel, UserDetailResponse
from typing import Optional


class PatientModel(BaseModel):
    id: str
    full_name: str
    phone_number: str
    appointment_date: Optional[str]
    medical_record: Optional[int]


class PatientResponseModel(BaseResponseModel):
    data: PatientModel

class ListPatientsModel(BaseResponseModel):
    data: list[PatientModel]


class AddPatientModel(AddUserModel):
    pass

class AddPatientResponseModel(BaseResponseModel):
    data: PatientResponseModel

class NewPatientModel(BaseModel):
    username: str
    password: str
    user_id: str


class NewPatientReponseModel(BaseResponseModel):
    data: NewPatientModel


class PatientDetailModel(BaseModel):
    appointment_date: Optional[str]
    medical_record: Optional[int]
    personal_info: UserDetailResponse


class PatientDetailResponseModel(BaseResponseModel):
    data: PatientDetailModel


class PatchPatientModel(PatchUserDetailModel):
    pass


class QueryPatientModel(BaseModel):
    user_id: Optional[str]
