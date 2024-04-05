from util.log import logger
from fastapi import HTTPException, Depends, status
from models.user import UserDetail
from models.employee import (
  EmployeeModel, 
  EmployeeDetailModel, 
  QueryEmployeeModel
)
from permissions import Permission
from permissions.user import UserRole
from repository.employee import EmployeeRepo
from repository.user import UserRepo
from middleware.user_ctx import UserContext

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

    
    @Permission.permit([UserRole.ADMIN])
    async def get_employees(self, employee_type, page: int = 1, employee_per_page: int = 10):
        page = 1 if page < 1 else page
        employee_per_page = 1 if employee_per_page < 0 else employee_per_page
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
            logger.error('Error in fetching employee list', reason=e)
            raise HTTPException(
                status_code=500, detail='Error in converting employee list')
        
        return employees
    
    @Permission.permit([UserRole.ADMIN, UserRole.EMPLOYEE])
    async def get(self, query: QueryEmployeeModel):
        if Permission.has_role([UserRole.EMPLOYEE], self._current_user):
            if self._current_user['sub'] != query.user_id:
                raise HTTPException(status_code=403, detail='Permission denied')
        employee, error = await self._employee_repo.get(query)
        if error:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error in fetching employee"
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
        