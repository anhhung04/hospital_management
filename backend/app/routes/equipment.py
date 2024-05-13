from fastapi import APIRouter, Depends, Query
from fastapi import HTTPException, status
from typing import Annotated
from services.equipment import EquipmentService
from util.response import APIResponse
from models.equipment import(
    EquipmentModel,
    EquipmentRequestModel,
    EquipmentListResponseModel,
    EquipmentBatchListResponseModel,
    EquipmentBatchModel,
    EquipmentBatchRequestModel,
)
from models.request import IdPath


router = APIRouter(tags=["equipment"])

@router.get("/list", response_model=EquipmentListResponseModel)
async def list_equipments(
    page: Annotated[int, Query(gt=0)] = 1,
    limit: Annotated[int, Query(gt=0)] = 10,
    service: EquipmentService = Depends(EquipmentService)
):
    try:
        equipments = await service.list_equipments(
            page, limit
        )
    except HTTPException as error:
        return APIResponse.as_json(
            code=error.status_code, message=str(error.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, data=equipments, message="Equipments fetched successfully"
    )

@router.get("/{equipment_id}", response_model=EquipmentModel)
async def get_equipment(
    equipment_id: IdPath,
    service: EquipmentService = Depends(EquipmentService)
):
    try:
        equipment = await service.get(
            id=str(equipment_id)
        )
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code, message=str(e.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, data=equipment, message="Equipment fetched successfully"
    )

@router.post("/create", response_model=EquipmentModel)
async def create_equipment(
    new_equipment_request: EquipmentRequestModel,
    service: EquipmentService = Depends(EquipmentService)
):
    try:
        equipment = await service.create(new_equipment_request)
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code, message=str(e.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, data=equipment, message="Equipment created successfully"
    )

@router.get("/{equipment_id}/batch/list", response_model=EquipmentBatchListResponseModel)
async def list_batches(
    equipment_id: IdPath,
    page: Annotated[int, Query(gt=0)] = 1,
    limit: Annotated[int, Query(gt=0)] = 10,
    service: EquipmentService = Depends(EquipmentService)
):
    try:
        batches = await service.list_batches(
            equipment_id=str(equipment_id), page=page, batches_per_page=limit
        )
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code, message=str(e.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, data=batches, message="Batches fetched successfully"
    )

@router.get("/{equipment_id}/batch/{batch_id}", response_model=EquipmentBatchModel)
async def get_batch(
    equipment_id: IdPath,
    batch_id: IdPath,
    service: EquipmentService = Depends(EquipmentService)
):
    try:
        batch = await service.get_batch(
            equipment_id=str(equipment_id), batch_id=str(batch_id)
        )
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code, message=str(e.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, data=batch, message="Batch fetched successfully"
    )

@router.post("/{equipment_id}/batch/create", response_model=EquipmentBatchModel)
async def create_batch(
    equipment_id: IdPath,
    new_batch_request: EquipmentBatchRequestModel,
    service: EquipmentService = Depends(EquipmentService)
):
    try:
        batch = await service.create_batch(
            equipment_id=str(equipment_id), batch=new_batch_request
        )
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code, message=str(e.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, data=batch, message="Batch created successfully"
    )