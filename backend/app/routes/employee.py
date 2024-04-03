from fastapi import APIRouter, Depends, Request
from services.employee import EmployeeService
from repository import Storage
from fastapi import Query, Path, HTTPException, status
from typing import Annotated
from util.response import APIResponse
from models.employee import ListEmployeeModel

router = APIRouter(tags=["employee"])

@router.get("/list", response_model=ListEmployeeModel)
async def list_employees(
    employee_type: str,
    request: Request,
    page: Annotated[int, Query(gt=0)] = 1,
    employee_per_page: Annotated[int, Query(gt=0)] = 10,
    db_sess=Depends(Storage.get)
):
    try:
        employees = await EmployeeService(db_sess, request.state.user).get_employees(employee_type, page, employee_per_page)
    except HTTPException as error:
        return APIResponse.as_json(
            code=error.status_code, message=str(error.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, data=employees, message="Employees fetched successful"
    )
        