from pydantic import BaseModel
from models.response import BaseResponseModel
from typing import Optional
from models.user import UserDetail
from repository.schemas.employees import EmployeeStatus, EducateLevel
from permissions.user import EmployeeType
from enum import Enum

class EmployeeModel(BaseModel):
    id: str
    full_name: str
    falcuty: str
    status: EmployeeStatus

class ListEmployeeModel(BaseResponseModel):
    data: list[EmployeeModel]

class EmployeeDetailModel(BaseModel):
    employee_type: EmployeeType
    educational_level: EducateLevel
    begin_date: str
    end_date: str
    faculty: str
    status: EmployeeStatus
    personal_info: UserDetail

class EmployeeDetailReponseModel(BaseResponseModel):
    data: EmployeeDetailModel

class AddEmployeeRequestModel(BaseModel):
    first_name: str
    last_name: str
    birth_date: str
    gender: str
    ssn: str
    phone_number: str
    address: str
    email: Optional[str]
    health_insurance: Optional[str]

class NewEmployeeModel(BaseModel):
    username: str
    password: str
    user_id: str

class NewEmployeeResponseModel(BaseResponseModel):
    data: NewEmployeeModel

class QueryEmployeeModel(BaseModel):
    user_id: str

class EmployeeTypeQueryModel(str, Enum):
    ALL = 'all'
    DOCTOR = 'doctor'
    NURSE = 'nurse'
    OTHER = 'other'
