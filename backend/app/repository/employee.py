from collections import namedtuple
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
from models.event import(
  PatchEventRequestModel, 
  AddEventModel
)
from repository.schemas.employees import(
  Employee, 
  EmployeeStatus, EducateLevel, 
  Event, DayOfWeek, Frequency, schedule
)
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
            if employee_type is not None:
                query = query.filter(Employee.employee_type == employee_type)
            query = query.limit(employee_per_page).offset(
                (page - 1) * employee_per_page
            )
            employees = query.all()
        except Exception as e:
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
    

    async def list_events(
        self,
        query: QueryEmployeeModel
    ) -> Tuple[list[Event], Exception | None]:
        try:
            events = self._sess.query(Event).join(schedule).filter(
                schedule.c.employee_id == query.user_id
            ).all()
            # events = query.filter(Event.begin_date >= begin_date, Event.begin_date <= end_date).all()
        except Exception as e:
            return [], e
        return events, None
    
    async def create_event(
        self,
        event_info: AddEventModel,
        employee_id: str
    ) -> Tuple[Event, Exception | None]:
        try:
            event = Event(
                id=event_info.id,
                title=event_info.title,
                day_of_week=DayOfWeek(event_info.day_of_week),
                begin_time=event_info.begin_time,
                end_time=event_info.end_time,
                begin_date=event_info.begin_date,
                end_date=event_info.end_date,
                is_recurring=event_info.is_recurring,
                frequency=Frequency(event_info.frequency)
            )
            employee = self._sess.query(Employee).filter(
                Employee.user_id == employee_id
            ).first()
            employee.event.append(event)
            self._sess.add(event)
            self._sess.commit()
        except IntegrityError as e:
            self._sess.rollback()
            return None, e
        except Exception as e:
            return None, e
        return event, None
        
    async def get_event(
        self,
        query: QueryEmployeeModel,
        event_id: str
    ) -> Tuple[Event, Exception | None]:
        try:
            event = self._sess.query(Event).join(schedule).filter(
                schedule.c.employee_id == query.user_id,
                Event.id == event_id
            ).first()
        except Exception as e:
            return None, e
        return event, None
    
    async def update_event(
        self,
        query: QueryEmployeeModel,
        event_id: str,
        patch_event: PatchEventRequestModel
    ) -> Tuple[Event, Exception | None]:
        try:
            event, error = await self.get_event(query, event_id)
            if error:
                return None, error
            new_event_dict = patch_event.model_dump()
            for attr, value in new_event_dict.items():
                if value is not None:
                    if attr == "frequency":
                        value = Frequency(value)
                    setattr(
                        event,
                        attr,
                        value
                    )
            self._sess.add(event)
            self._sess.commit()
            self._sess.refresh(event)
        except IntegrityError as e:
            self._sess.rollback()
            return None, e
        except Exception as e:
            return None, e
        return event, None
    
    async def delete_event(
        self,
        query: QueryEmployeeModel,
        event_id: str
    ) -> Exception | None:
        try:
            event = self._sess.query(Event).join(schedule).filter(
                schedule.c.employee_id == query.user_id,
                Event.id == event_id
            ).first()
            self._sess.delete(event)
            self._sess.commit()
        except Exception as e:
            self._sess.rollback()
            return e
        return None

    async def count(self, type: EmployeeType | None = None):
        try:
            query = self._sess.query(Employee)
            if type:
                query = query.filter(Employee.employee_type == type)
            return query.count(), None
        except Exception as err:
            return 0, err
