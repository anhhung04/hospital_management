from fastapi import APIRouter, Depends, Request
from services.employee import EmployeeService
from repository import Storage
from fastapi import Query, Path, HTTPException, status
from typing import Annotated
from util.response import APIResponse
from models.employee import(
  ListEmployeeModel, 
  EmployeeDetailReponseModel, 
  NewEmployeeResponseModel, 
  AddEmployeeRequestModel,
  QueryEmployeeModel,
  EmployeeTypeQueryModel
)


router = APIRouter(tags=["employee"])

# @router.get("/list/{employee_type}", response_model=ListEmployeeModel)
# async def list_employees(
#     employee_type: EmployeeTypeQueryModel,
#     page: Annotated[int, Query(gt=0)] = 1,
#     employee_per_page: Annotated[int, Query(gt=0)] = 10,
#     service: EmployeeService = Depends(EmployeeService)
# ):
#     try:
#         employees = await service.get_employees(
#             employee_type, page, employee_per_page
#         )
#     except HTTPException as error:
#         return APIResponse.as_json(
#             code=error.status_code, message=str(error.detail), data={}
#         )
#     return APIResponse.as_json(
#         code=status.HTTP_200_OK, data=employees, message="Employees fetched successful"
#     )

@router.get("/{employee_id}", response_model=EmployeeDetailReponseModel)
async def get_employee(
    employee_id: Annotated[str, Path(regex=r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")],
    service: EmployeeService = Depends(EmployeeService)
):
    try:
        employee = await service.get(
            QueryEmployeeModel(user_id=employee_id)
        )
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code, message=str(e.detail), data={})
    return APIResponse.as_json(
        code=status.HTTP_200_OK, data=employee, message="Employee fetched successful"
    )
        
@router.post("/create", response_model=NewEmployeeResponseModel)
async def create_employee(
    new_user: AddEmployeeRequestModel,
    request: Request,
    db_sess=Depends(Storage.get)
):
    try:
        employee = await EmployeeService(db_sess, request.state.user).create(new_user.model_dump())
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code, message=str(e.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, message="Employee created successfully", data=employee
    )