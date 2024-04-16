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
  AddEmployeeModel,
  PatchEmployeeModel
)
from repository.schemas.employees import EmployeeStatus, EducateLevel
from permissions.user import EmployeeType

GetEmployeeQuery = namedtuple("GetEmployeeQuery", ["id", "username"])

attribute_mapping = {
  "employee_type": EmployeeType,
  "education_level": EducateLevel,
  "status": EmployeeStatus
}

class EmployeeRepo:
    def __init__(
        self,
        user_repo: UserRepo=Depends(UserRepo),
        session: Session = Depends(Storage.get)
    ):
      self._sess = session
      self._user_repo = user_repo

    async def list_employees(self, employee_type: EmployeeType | None, page: int, employee_per_page: int) -> Tuple[list[Employee], Exception | None]:
        try:
            query = self._sess.query(Employee)
            if employee_type:
                query = query.filter(Employee.employee_type == employee_type)
            query = query.limit(employee_per_page).offset(
                (page - 1) * employee_per_page
            )
            employees = query.all()
        except Exception as e:
            print(e)
            return [], e
        return employees, None
    
    async def get(self, query: QueryEmployeeModel) -> Tuple[Employee, Exception | None]:
        try:
            employee = self._sess.query(Employee).filter(
                Employee.user_id == query.user_id).first()
        except Exception as e:
            return None, e
        return employee, None
    
    async def create(self, employee_info: AddEmployeeModel) -> Tuple[Employee, Exception | None]:
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

    async def update(
        self, 
        query: QueryEmployeeModel, 
        employee_update: PatchEmployeeModel
    ) -> Tuple[Employee, Exception | None]:
        try:
            employee, error = await self.get(query)
            if error:
                return None, error
            new_employee_dict = employee_update.model_dump()
            for attr, value in new_employee_dict.items():
                if value:
                    if attr == "personal_info":
                        for _attr, _value in new_employee_dict.get("personal_info", {}).items():
                            setattr(
                                employee.personal_info,
                                _attr,
                                _value
                            ) if _value else None
                    else: 
                        if attr in attribute_mapping:
                            value = attribute_mapping[attr](value)
                        setattr(
                            employee,
                            attr,
                            value
                        )            
            self._sess.add(employee)
            self._sess.commit()
            self._sess.refresh(employee)
        except Exception as e:
            self._sess.rollback()
            return None, e
        return employee, None