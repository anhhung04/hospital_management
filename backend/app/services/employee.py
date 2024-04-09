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
from permissions import Permission
from permissions.user import UserRole, EmployeeType
from repository.employee import EmployeeRepo
from repository.user import UserRepo
from middleware.user_ctx import UserContext
from util.crypto import PasswordContext
from uuid import uuid4

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

    
    @Permission.permit([UserRole.ADMIN, UserRole.EMPLOYEE, EmployeeType.MANAGER])
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
    
    @Permission.permit([UserRole.ADMIN, EmployeeType.MANAGER]) # Cần fix chỗ này
    async def get(self, query: QueryEmployeeModel):
        if Permission.has_role([UserRole.EMPLOYEE], self._current_user):
            if self._current_user.id() != query.user_id:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN, 
                    detail='Permission denied'
                )
        employee, error = await self._employee_repo.get(query)
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
    
    @Permission.permit([UserRole.ADMIN, UserRole.EMPLOYEE]) #Cần xóa employee
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
    
    @Permission.permit([UserRole.ADMIN, UserRole.EMPLOYEE])
    async def update(self, query: QueryEmployeeModel, employee_update: PatchEmployeeModel):
        if Permission.has_role([UserRole.EMPLOYEE], self._current_user):
            if self._current_user.id() != query.user_id:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN, 
                    detail='Permission denied'
                )
        employee, error = await self._employee_repo.update(
            QueryEmployeeModel.model_validate(query),
            employee_update
        )
        if error:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error in update employee information"
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
            
    @Permission.permit([UserRole.ADMIN, UserRole.EMPLOYEE])
    async def get_events(self, query: QueryEmployeeModel):
        if Permission.has_role([UserRole.EMPLOYEE], self._current_user):
            if self._current_user.id() != query.user_id:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN, 
                    detail='Permission denied'
                )
        events, error = await self._employee_repo.get_events(query)
        if error:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error in fetching employee events"
            )
        return events
