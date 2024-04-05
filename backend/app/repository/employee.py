from collections import namedtuple
from repository.schemas.employees import Employee 
from repository.user import UserRepo
from repository.schemas.user import User
from typing import Tuple
from fastapi import Depends
from repository import Storage
from sqlalchemy.orm import Session

GetEmployeeQuery = namedtuple("GetEmployeeQuery", ["id", "username"])

class EmployeeRepo:
    def __init__(
        self,
        user_repo: UserRepo=Depends(UserRepo),
        session: Session = Depends(Storage.get)
    ):
      self._sess = session
      self._user_repo = user_repo

    async def list_employees(self, employee_type: str, page: int, employee_per_page: int) -> list[Employee]:
        try:
            query = self._sess.query(Employee)
            if employee_type != "all" and employee_type != "other":
                query = query.filter(Employee.employee_type == employee_type)
            elif employee_type == "other":
               query = query.filter(Employee.employee_type != 'doctor' | Employee.employee_type != 'nurse') 
            employees = query.limit(employee_per_page).offset((page - 1) * employee_per_page).all()
        except Exception as e:
          return [], e
        return employees, None
    
    async def get(self, employee_id: str) -> Employee:
        try:
          employee = self._sess.query(Employee).filter(
              Employee.user_id == employee_id).first()
        except Exception as e:
          return None
        return employee

