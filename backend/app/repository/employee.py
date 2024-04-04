from collections import namedtuple
from repository.schemas.employee import Employee 
from repository.user import UserRepo
from repository.schemas.user import User
from typing import Tuple

GetEmployeeQuery = namedtuple("GetEmployeeQuery", ["id", "username"])

class EmployeeRepo:
    def __init__(self, session):
      self._sess = session
      self._user_repo = UserRepo(session)

    async def list_employees(self, employee_type: str, page: int, employee_per_page: int) -> list[Employee]:
        try:
            query = self._sess.query(Employee)
            if employee_type != "all":
                query = query.filter(Employee.employee_type == employee_type)
            employees = query.limit(employee_per_page).offset((page - 1) * employee_per_page).all()
        except Exception:
          return []
        return employees
    
    async def get(self, employee_id: str) -> Employee:
        try:
          employee = self._sess.query(Employee).filter(
              Employee.user_id == employee_id).first()
        except Exception as e:
          return None
        return employee

