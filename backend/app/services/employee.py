from util.log import logger
from fastapi import HTTPException, Depends, status
from models.user import UserDetail, AddUserDetailModel
from models.employee import (
  EmployeeModel, 
  EmployeeDetailModel, 
  QueryEmployeeModel,
  AddEmployeeRequestModel,
  AddEmployeeModel,
  PatchEmployeeModel
)
from models.event import(
  EventModel,
  day_of_week_map,
  freq_map,
  EventRequestModel,
  ListEventModel,
  PatchEventRequestModel,
  AddEventModel
)
from permissions import Permission
from permissions.user import UserRole, EmployeeType
from repository.employee import EmployeeRepo
from repository.user import UserRepo
from middleware.user_ctx import UserContext
from util.crypto import PasswordContext
from uuid import uuid4
from datetime import date, timedelta
from dateutil.rrule import rrule

class EmployeeService:
    def __init__(
        self, 
        user: UserContext=Depends(UserContext),
        employee_repo: EmployeeRepo=Depends(EmployeeRepo),
        user_repo: UserRepo=Depends(UserRepo)
    ):
        self._current_user = user
        self._employee_repo = employee_repo
        self._user_repo = user_repo

    
    @Permission.permit([EmployeeType.MANAGER])
    async def get_employees(self, employee_type: EmployeeType | None, page: int = 1, employee_per_page: int = 10):
        page = 1 if page < 1 else page
        employee_per_page = 1 if employee_per_page <= 0 else employee_per_page
        employees, error = await self._employee_repo.list_employees(employee_type, page, employee_per_page)
        if error:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                                detail="Error in fetching employees list")
        try:
            employees = [EmployeeModel(
                id=employee.user_id,
                full_name=" ".join(
                    [employee.personal_info.last_name, employee.personal_info.first_name]),
                faculty=employee.faculty,
                status=employee.status
            ).model_dump() for employee in employees]
        except Exception as e:
            logger.error('Error in converting employee list', reason=e)
            raise HTTPException(
                status_code=500, detail='Error in converting employee list')
        
        return employees
    
    @Permission.permit([EmployeeType.MANAGER], acl=[UserRole.EMPLOYEE])
    async def get(self, id: str):
        employee, error = await self._employee_repo.get(
            query=QueryEmployeeModel(user_id=id)
        )
        if error:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error in fetching employee information"
            )
        if not employee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail='Employee not found'
            )
        return EmployeeDetailModel(
            employee_type=employee.employee_type,
            educational_level=employee.education_level,
            begin_date=str(employee.begin_date),
            end_date=str(employee.end_date),
            faculty=employee.faculty,
            status=employee.status,
            personal_info=UserDetail.model_validate(
                obj=employee.personal_info, strict=False, from_attributes=True
            )
        ).model_dump()
    
    @Permission.permit([EmployeeType.MANAGER])
    async def create(self, employee: AddEmployeeRequestModel):
        raw_password = PasswordContext.rand_key()
        username = f"employee_{employee.ssn}"
        user_info = employee.model_dump()
        employee_id = str(uuid4())
        if not employee.employee_type:
            employee.employee_type = EmployeeType.OTHER
        user_info.update({
            "id": employee_id,
            "username": username,
            "password": PasswordContext(raw_password, username).hash(),
            "role": Permission(UserRole.EMPLOYEE).add(employee.employee_type).get(),
        })
        employee_info = {
            "user_id": employee_id,
            "education_level": None,
            "begin_date": None,
            "end_date": None,
            "faculty": None,
            "status": None,
            "employee_type": employee.employee_type,
            "personal_info": AddUserDetailModel.model_validate(user_info).model_dump()
        }
        employee_in_db, error = await self._employee_repo.create(
            AddEmployeeModel.model_validate(employee_info)
        )
        if employee_in_db:
            return {
                "username": employee_in_db.personal_info.username,
                "password": raw_password,
                "user_id": employee_in_db.user_id
            }
        if error or not employee_in_db:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error in create employee"
            )
    
    @Permission.permit([EmployeeType.MANAGER], acl=[UserRole.EMPLOYEE])
    async def update(self, id: str, employee_update: PatchEmployeeModel):
        employee, error = await self._employee_repo.update(
            QueryEmployeeModel.model_validate(QueryEmployeeModel(user_id=id)),
            employee_update
        )
        if error:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error in update employee information"
            )
        return EmployeeDetailModel(
            employee_type=employee.employee_type,
            education_level=employee.education_level,
            begin_date=str(employee.begin_date),
            end_date=str(employee.end_date),
            faculty=employee.faculty,
            status=employee.status,
            personal_info=UserDetail.model_validate(
                obj=employee.personal_info, strict=False, from_attributes=True
            )
        ).model_dump()
    
    @Permission.permit([EmployeeType.MANAGER], acl=[UserRole.EMPLOYEE])
    async def list_events(self, id: str, begin_date: date, end_date: date):
        if not begin_date:
            current_date = date.today()
            days_to_monday = current_date.weekday()
            begin_date = current_date - timedelta(days=days_to_monday)
            end_date = begin_date + timedelta(days=6)
        if not end_date:
            end_date = begin_date + timedelta(days=6)
        if begin_date > end_date:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Begin date must be less than or equal end date"
            )
        events, error = await self._employee_repo.list_events(
            query=QueryEmployeeModel(user_id=id),
            begin_date=begin_date, 
            end_date=end_date
        )
        if error:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error in fetching employee events"
            )
        events = [ListEventModel(
            id=event.id,
            title=event.title,
            day_of_week=str(event.day_of_week.value),
            begin_time=event.begin_time.strftime("%H:%M"),
            end_time=event.end_time.strftime("%H:%M"),
            begin_date=str(event.begin_date),
            end_date=str(event.end_date) if event.end_date else None,
            is_recurring=event.is_recurring,
            frequency=event.frequency.value if event.frequency else None,
            occurence=[date.strftime("%Y-%m-%d") for date in list(rrule(
                freq=freq_map[event.frequency.value],
                dtstart=event.begin_date,
                until=min(end_date, event.end_date) if event.end_date and end_date else end_date,
                byweekday=day_of_week_map[event.day_of_week.value]
            ))] if event.is_recurring else [str(event.begin_date)]
        ).model_dump() for event in events]
        return events
    
    @Permission.permit([EmployeeType.MANAGER], acl=[UserRole.EMPLOYEE])
    async def create_event(
        self, 
        id: str, 
        event: EventRequestModel
    ):
        try:
            event_info = event.model_dump()
            event_id = str(uuid4())
            event_info.update({"id": event_id})
            event_in_db, error = await self._employee_repo.create_event(
                AddEventModel.model_validate(event_info),
                employee_id=id
            )
            if error or not event_in_db:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Error in creating event"
                )
            return EventModel(
                id=event_in_db.id,
                title=event_in_db.title,
                day_of_week=str(event_in_db.day_of_week.value),
                begin_time=event_in_db.begin_time.strftime("%H:%M"),
                end_time=event_in_db.end_time.strftime("%H:%M"),
                begin_date=str(event_in_db.begin_date),
                end_date=str(event_in_db.end_date) if event_in_db.end_date else None,
                is_recurring=event_in_db.is_recurring,
                frequency=event_in_db.frequency.value if event_in_db.frequency else None
            ).model_dump()
        except Exception as e:
            logger.error('Error in creating event', reason=e)
            raise HTTPException(
                status_code=500, detail='Error in creating event'
            )
        
    @Permission.permit([EmployeeType.MANAGER], acl=[UserRole.EMPLOYEE])
    async def get_event(self, id: str, event_id: str):
        event, error = await self._employee_repo.get_event(
            query=QueryEmployeeModel(user_id=id),
            event_id=event_id
        )
        if error:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error in fetching event"
            )
        if not event:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Event not found"
            )
        return EventModel(
            id=event.id,
            title=event.title,
            day_of_week=str(event.day_of_week.value),
            begin_time=event.begin_time.strftime("%H:%M"),
            end_time=event.end_time.strftime("%H:%M"),
            begin_date=str(event.begin_date),
            end_date=str(event.end_date) if event.end_date else None,
            is_recurring=event.is_recurring,
            frequency=event.frequency.value if event.frequency else None
        ).model_dump()
    
    @Permission.permit([EmployeeType.MANAGER], acl=[UserRole.EMPLOYEE])
    async def update_event(
        self,
        id: str,
        event_id: str,
        patch_event: PatchEventRequestModel
    ):
        event, error = await self._employee_repo.update_event(
            QueryEmployeeModel(user_id=id),
            event_id=event_id,
            patch_event=patch_event
        )
        if error:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error in updating event"
            )
        return EventModel(
            id=event.id,
            title=event.title,
            day_of_week=str(event.day_of_week.value),
            begin_time=event.begin_time.strftime("%H:%M"),
            end_time=event.end_time.strftime("%H:%M"),
            begin_date=str(event.begin_date),
            end_date=str(event.end_date)
        ).model_dump()
    
    @Permission.permit([EmployeeType.MANAGER], acl=[UserRole.EMPLOYEE])
    async def delete_event(self, id: str, event_id: str):
        error = await self._employee_repo.delete_event(
            QueryEmployeeModel(user_id=id),
            event_id=event_id
        )
        if error:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error in deleting event"
            )