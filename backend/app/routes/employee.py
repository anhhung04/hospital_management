from fastapi import APIRouter, Depends, Query
from services.employee import EmployeeService
from fastapi import HTTPException, status
from util.response import APIResponse
from models.employee import(
  ListEmployeeModel, 
  EmployeeDetailReponseModel, 
  NewEmployeeResponseModel, 
  AddEmployeeRequestModel,
  QueryEmployeeModel,
  PatchEmployeeModel
)
from models.request import IdPath
from permissions.user import EmployeeType
from typing import Annotated

router = APIRouter(tags=["employee"])

@router.get("/list", response_model=ListEmployeeModel)
async def list_employees(
    type: Annotated[EmployeeType | None, Query] = None,
    page: Annotated[int, Query(gt=0)] = 1,
    employee_per_page: Annotated[int, Query(gt=0)] = 10,
    service: EmployeeService = Depends(EmployeeService)
):
    try:
        employees = await service.get_employees(
            type, page, employee_per_page
        )
    except HTTPException as error:
        return APIResponse.as_json(
            code=error.status_code, message=str(error.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, data=employees, message="Employees fetched successful"
    )

@router.get("/{employee_id}", response_model=EmployeeDetailReponseModel)
async def get_employee(
    employee_id: IdPath,
    service: EmployeeService = Depends(EmployeeService)
):
    try:
        employee = await service.get(
            id=employee_id
        )
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code, message=str(e.detail), data={})
    return APIResponse.as_json(
        code=status.HTTP_200_OK, data=employee, message="Employee fetched successful"
    )
        
@router.post("/create", response_model=NewEmployeeResponseModel)
async def create_employee(
    new_employee_request: AddEmployeeRequestModel,
    service: EmployeeService = Depends(EmployeeService)
):
    try:
        employee = await service.create(new_employee_request)
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code, message=str(e.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, message="Employee created successfully", data=employee
    )

@router.patch("/{employee_id}/update", response_model=EmployeeDetailReponseModel)
async def update_employee(
    employee_id: IdPath,
    employee_update: PatchEmployeeModel,
    service: EmployeeService = Depends(EmployeeService)
):
    try:
        employee = await service.update(
            QueryEmployeeModel(user_id=employee_id),
            employee_update
        )
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code, message=str(e.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, message="Employee updated successfully", data=employee
    )
