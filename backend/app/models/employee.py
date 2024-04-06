from pydantic import BaseModel, ConfigDict
from models.response import BaseResponseModel
from typing import Optional
from models.user import UserDetail, AddUserModel, AddUserDetailModel
from repository.schemas.employees import EmployeeStatus, EducateLevel
from permissions.user import EmployeeType
from enum import Enum

class EmployeeModel(BaseModel):
    id: str
    full_name: str
    faculty: str
    status: Optional[EmployeeStatus | None] = None

class ListEmployeeModel(BaseResponseModel):
    data: list[EmployeeModel]

class EmployeeDetailModel(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    employee_type: EmployeeType
    educational_level: EducateLevel
    begin_date: str
    end_date: str
    faculty: str
    status: Optional[EmployeeStatus | None] = None
    personal_info: UserDetail

class EmployeeDetailReponseModel(BaseResponseModel):
    data: EmployeeDetailModel

class AddEmployeeRequestModel(AddUserModel):
    pass

class AddEmployeeModel(BaseModel):
    model_config = ConfigDict(use_enum_values=True)    

    user_id: str
    employee_type: Optional[EmployeeType | None] = None
    education_level: Optional[EducateLevel | None] = None
    begin_date: Optional[str | None] = None
    end_date: Optional[str | None] = None
    faculty: Optional[str | None] = None
    status: Optional[str | None] = None
    personal_info: AddUserDetailModel

class NewEmployeeModel(BaseModel):
    username: str
    password: str
    user_id: str

class NewEmployeeResponseModel(BaseResponseModel):
    data: NewEmployeeModel

class QueryEmployeeModel(BaseModel):
    user_id: str

class EmployeeTypeModel(str, Enum):
    ALL = 'all'
    DOCTOR = 'doctor'
    NURSE = 'nurse'
    OTHER = 'other'
