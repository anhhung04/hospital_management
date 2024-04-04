from pydantic import BaseModel
from models.response import BaseResponseModel
from typing import Optional
from models.user import UserDetail
from repository.schemas.employee import EmployeeStatus, EducateLevel

class EmployeeModel(BaseModel):
    id: str
    full_name: str
    falcuty: str
    status: EmployeeStatus

class ListEmployeeModel(BaseResponseModel):
    data: list[EmployeeModel]

class EmployeeDetailModel(UserDetail):
    employee_type: str
    educational_level: EducateLevel
    begin_date: str
    end_date: str
    faculty: str
    status: EmployeeStatus

class EmployeeDetailReponseModel(BaseResponseModel):
    data: EmployeeDetailModel



