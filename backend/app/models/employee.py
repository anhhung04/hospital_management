from pydantic import BaseModel
from models.response import BaseResponseModel
from typing import Optional
from models.user import UserDetail

class EmployeeModel(BaseModel):
    id: str
    full_name: str
    falcuty: str
    # Scheduling_state

class ListEmployeeModel(BaseResponseModel):
    data: list[EmployeeModel]

