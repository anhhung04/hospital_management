from fastapi import APIRouter, Depends, Query
from fastapi import HTTPException, status
from typing import Annotated
from services.medicine import MedicineService
from util.response import APIResponse
from models.medicine import(
    MedicineModel,
    MedicineRequestModel,
    MedicineListResponseModel,
    MedicineBatchModel,
    MedicineBatchRequestModel,
    MedicineBatchListResponseModel,
)
from models.request import IdPath

router = APIRouter(tags=["medicine"])

@router.get("/list", response_model=MedicineListResponseModel)
async def list_medicines(
    page: Annotated[int, Query(gt=0)] = 1,
    medicine_per_page: Annotated[int, Query(gt=0)] = 10,
    service: MedicineService = Depends(MedicineService)
):
    try:
        medicines = await service.list_medicines(
            page, medicine_per_page
        )
    except HTTPException as error:
        return APIResponse.as_json(
            code=error.status_code, message=str(error.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, data=medicines, message="Medicines fetched successfully"
    )

@router.get("/{medicine_id}", response_model=MedicineModel)
async def get_medicine(
    medicine_id: IdPath,
    service: MedicineService = Depends(MedicineService)
):
    try:
        medicine = await service.get(
            id=str(medicine_id)
        )
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code, message=str(e.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, data=medicine, message="Medicine fetched successfully"
    )

@router.post("/create", response_model=MedicineModel)
async def create_medicine(
    new_medicine_request: MedicineRequestModel,
    service: MedicineService = Depends(MedicineService)
):
    try:
        medicine = await service.create(new_medicine_request)
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code, message=str(e.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, data=medicine, message="Medicine created successfully"
    )

@router.get("/{medicine_id}/batch/list", response_model=MedicineBatchListResponseModel)
async def get_batches(
    medicine_id: IdPath,
    page: Annotated[int, Query(gt=0)] = 1,
    batches_per_page: Annotated[int, Query(gt=0)] = 10,
    service: MedicineService = Depends(MedicineService)
):
    try:
        batches = await service.list_batches(
            medicine_id=str(medicine_id),
            page=page,
            batches_per_page=batches_per_page
        )
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code, message=str(e.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, data=batches, message="Batches fetched successfully"
    )

@router.get("/{medicine_id}/batch/{batch_id}", response_model=MedicineBatchModel)
async def get_batch(
    medicine_id: IdPath,
    batch_id: IdPath,
    service: MedicineService = Depends(MedicineService)
):
    try:
        batch = await service.get_batch(
            medicine_id=str(medicine_id),
            batch_id=str(batch_id)
        )
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code, message=str(e.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, data=batch, message="Batch fetched successfully"
    )


@router.post("/{medicine_id}/batch/create", response_model=MedicineBatchModel)
async def create_batch(
    medicine_id: IdPath,
    new_batch_request: MedicineBatchRequestModel,
    service: MedicineService = Depends(MedicineService)
):
    try:
        batch = await service.create_batch(
            medicine_id=str(medicine_id),
            batch=new_batch_request
        )
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code, message=str(e.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, data=batch, message="Batch created successfully"
    )