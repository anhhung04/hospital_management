from pydantic import BaseModel
from models.response import BaseResponseModel
from models.user import PatchUserDetailModel, UserDetail, AddUserModel
from models.medical_record import MedicalRecordModel
from typing import Optional


class PatientModel(BaseModel):
    id: str
    full_name: str
    phone_number: str
    appointment_date: Optional[str | None] = None
    medical_record_id: Optional[int | None] = None

class PatientResponseModel(BaseResponseModel):
    data: PatientModel

class ListPatientsModel(BaseResponseModel):
    data: list[PatientModel]


class AddPatientModel(BaseModel):
    user_id: str


class AddPatientRequestModel(AddUserModel):
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
    appointment_date: Optional[str | None] = None
    medical_record: Optional[MedicalRecordModel | None] = None
    personal_info: UserDetail


class PatientDetailResponseModel(BaseResponseModel):
    data: PatientDetailModel


class PatchPatientModel(PatchUserDetailModel):
    pass


class QueryPatientModel(BaseModel):
    user_id: Optional[str | None] = None
