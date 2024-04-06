from collections import namedtuple
from repository.schemas.employees import Employee 
from repository.user import UserRepo
from repository.schemas.user import User
from typing import Tuple
from fastapi import Depends
from repository import Storage
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.employee import(
  QueryEmployeeModel, 
  AddEmployeeModel
)

GetEmployeeQuery = namedtuple("GetEmployeeQuery", ["id", "username"])

class EmployeeRepo:
    def __init__(
        self,
        user_repo: UserRepo=Depends(UserRepo),
        session: Session = Depends(Storage.get)
    ):
      self._sess = session
      self._user_repo = user_repo

    async def list_employees(self, employee_type: str, page: int, employee_per_page: int) -> Tuple[list[Employee], Exception]:
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
    
    async def get(self, query: QueryEmployeeModel) -> Tuple[Employee, Exception]:
        try:
            employee = self._sess.query(Employee).filter(
                Employee.user_id == query.user_id).first()
        except Exception as e:
            return None, e
        return employee, None
    
    async def create(self, employee_info: AddEmployeeModel) -> Tuple[Employee, Exception]:
        try:
            new_employee = Employee(
                user_id=employee_info.user_id,
                employee_type=employee_info.employee_type,
                education_level=employee_info.education_level,
                begin_date=employee_info.begin_date,
                end_date=employee_info.end_date,
                faculty=employee_info.faculty,
                status=employee_info.status,
                personal_info=User(**employee_info.personal_info.model_dump())
            )
            self._sess.add(new_employee)
            self._sess.commit()
        except IntegrityError as e:
            self._sess.rollback()
            return None, e
        except Exception as e:
            return None, e
        return new_employee, None


