from fastapi import APIRouter, Depends, Query
from services.employee import EmployeeService
from fastapi import HTTPException, status
from util.response import APIResponse
from models.employee import(
  ListEmployeeModel, 
  EmployeeDetailReponseModel, 
  NewEmployeeResponseModel, 
  AddEmployeeRequestModel,
  PatchEmployeeModel,
)
from models.event import(
  ListEventResponseModel,
  EventRequestModel,
  EventReponseModel,
  PatchEventRequestModel
)
from models.request import IdPath
from permissions.user import EmployeeType
from typing import Annotated
from datetime import date
from uuid import UUID

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
            id=str(employee_id)
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
            id=str(employee_id),
            employee_update=employee_update
        )
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code, message=str(e.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, message="Employee updated successfully", data=employee
    )

@router.get("/{employee_id}/event", response_model=ListEventResponseModel)
async def list_events(
    employee_id: IdPath,
    begin_date: Annotated[date | None, Query] = None,
    end_date: Annotated[date | None, Query] = None,
    service: EmployeeService = Depends(EmployeeService)
):
    try:
        events = await service.list_events(
            id=str(employee_id),
            begin_date=begin_date,
            end_date=end_date
        )
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code, message=str(e.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, message="Events fetched successfully", data=events
    )

@router.get("/{employee_id}/event/{event_id}", response_model=EventReponseModel)
async def get_event(
    employee_id: IdPath,
    event_id: IdPath,
    service: EmployeeService = Depends(EmployeeService)
):
    try:
        event = await service.get_event(
            id=str(employee_id),
            event_id=str(event_id)
        )
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code, message=str(e.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, message="Event fetched successfully", data=event
    )

@router.post("/{employee_id}/event/create", response_model=EventReponseModel)
async def create_event(
    employee_id: IdPath,
    event_request: EventRequestModel,
    service: EmployeeService = Depends(EmployeeService)
):
    try:
        event = await service.create_event(
            id=str(employee_id),
            event=event_request
        ) 
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code, message=str(e.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, message="Event created successfully", data=event
    )

@router.patch("/{employee_id}/event/{event_id}/update", response_model=EventReponseModel)
async def update_event(
    employee_id: IdPath,
    event_id: IdPath,
    patch_event: PatchEventRequestModel,
    service: EmployeeService = Depends(EmployeeService)
):
    try:
        event = await service.update_event(
            id=str(employee_id),
            event_id=str(event_id),
            patch_event=patch_event
        )
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code, message=str(e.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, message="Event updated successfully", data=event
    )

@router.delete("/{employee_id}/event/{event_id}/delete")
async def delete_event(
    employee_id: IdPath,
    event_id: IdPath,
    service: EmployeeService = Depends(EmployeeService)
):
    try:
        await service.delete_event(
            id=str(employee_id),
            event_id=str(event_id)
        )
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code, message=str(e.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, message="Event deleted successfully", data={}
    )