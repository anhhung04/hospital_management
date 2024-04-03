from sqlalchemy.orm import Session
from services import IService
from util.log import logger
from fastapi import HTTPException
from models.employee import EmployeeModel 
from permissions import Permission
from permissions.user import UserRole
from repository.employee import EmployeeRepo
from repository.user import UserRepo

class EmployeeService(IService):
    def __init__(self, session=None, user: dict = None, redis_client=None) -> None:
        super().__init__(session, user, redis_client)
        self._employee_repo = EmployeeRepo(session)
        self._user_repo = UserRepo(session)
    
    @Permission.permit([UserRole.ADMIN])
    async def get_employees(self, employee_type, page: int = 1, employee_per_page: int = 10):
        if page < 1:
            page = 1
        if employee_per_page < 1: 
            employee_per_page = 10
        employees = await self._employee_repo.list_employees(employee_type, page, employee_per_page)
        try:
            employees = [EmployeeModel(
                id=employee.user_id,
                full_name=" ".join(
                    [employee.personal_info.last_name, employee.personal_info.first_name]),
                faculty=employee.faculty
            ).model_dump() for employee in employees]
        except Exception as e:
            logger.error('Error in fetching employee list', reason=e)
            raise HTTPException(
                status_code=500, detail='Error in fetching employee list')
        
        return employees