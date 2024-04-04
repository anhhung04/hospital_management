from sqlalchemy.orm import Session
from services import IService
from util.log import logger
from fastapi import HTTPException
from models.employee import EmployeeModel, EmployeeDetailModel
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
                faculty=employee.faculty,
                status=employee.status
            ).model_dump() for employee in employees]
        except Exception as e:
            logger.error('Error in fetching employee list', reason=e)
            raise HTTPException(
                status_code=500, detail='Error in fetching employee list')
        
        return employees
    
    @Permission.permit([UserRole.ADMIN, UserRole.EMPLOYEE])
    async def get(self, employee_id: str):
        if Permission.has_role([UserRole.EMPLOYEE], self._current_user):
            if self._current_user['sub'] != employee_id:
                raise HTTPException(status_code=403, detail='Permission denied')
        employee = await self._employee_repo.get(employee)
        if not employee:
            raise HTTPException(status_code=404, detail='Employee not found')
        return EmployeeDetailModel(
            id=employee.user_id,
            ssn=employee.personal_info.ssn,
            phone_number=employee.personal_info.phone_numer,
            address=employee.personal_info.address,
            email=employee.personal_info.email,
            health_insurance=employee.personal_info.health_insurance,
            username=employee.personal_info.username,
            role=employee.personal_info.role,
            first_name=employee.personal_info.first_name,
            last_name=employee.personal_info.last_name,
            birth_date=employee.personal_info.birth_date,
            gender=employee.personal_info.gender,
            employee_type=employee.employee_type,
            educational_level=employee.education_level,
            begin_date=str(employee.begin_date),
            end_date=str(employee.end_date),
            faculty=employee.faculty,
            status=employee.status
        ).model_dump()
        
    