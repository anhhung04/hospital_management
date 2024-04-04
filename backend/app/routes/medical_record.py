from fastapi import APIRouter, Depends, HTTPException, status, Path
from models.medical_record import (
    MedicalRecordResponseModel, NewMedicalRecordModel, QueryMedicalRecordModel, PatchMedicalRecordModel
)
from services.medical_record import MedicalRecordService
from util.response import APIResponse
from typing import Annotated

router = APIRouter()


@router.get("/patient/{patient_id}", tags=["medial_record"], response_model=MedicalRecordResponseModel)
async def get_medicalrecord(
    patient_id: Annotated[str, Path(regex=r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")],
    service: MedicalRecordService = Depends(MedicalRecordService)
):
    try:
        medical_record = await service.get(
            QueryMedicalRecordModel(patient_id=patient_id)
        )
    except HTTPException as e:
        return APIResponse.as_json(code=e.status_code, message=str(e.detail))
    return APIResponse.as_json(
        code=status.HTTP_200_OK,
        data=medical_record,
        message="Medical record fetched successfully"
    )


@router.get("/me", tags=["medial_record"], response_model=MedicalRecordResponseModel)
async def get_my_medicalrecord(
    service: MedicalRecordService = Depends(MedicalRecordService)
):
    try:
        medical_record = await service.get_me()
    except HTTPException as e:
        return APIResponse.as_json(code=e.status_code, message=str(e.detail))
    return APIResponse.as_json(
        code=status.HTTP_200_OK,
        data=medical_record,
        message="Medical record fetched successfully"
    )


@router.post("/create", tags=["medial_record"], response_model=MedicalRecordResponseModel)
async def create_new_medical_record(
    medical_record: NewMedicalRecordModel,
    service: MedicalRecordService = Depends(MedicalRecordService)
):
    try:
        medical_record = await service.create(
            medical_record
        )
    except HTTPException as e:
        return APIResponse.as_json(code=e.status_code, message=str(e.detail))
    return APIResponse.as_json(
        code=status.HTTP_201_CREATED,
        data=medical_record,
        message="Medical record created successfully"
    )


@router.patch("/update/{patient_id}", tags=["medial_record"], response_model=MedicalRecordResponseModel)
async def update_medical_record(
    patient_id: str,
    new_medical_record: PatchMedicalRecordModel,
    service: MedicalRecordService = Depends(MedicalRecordService)
):
    try:
        new_medical_record = await service.update(
            QueryMedicalRecordModel(patient_id=patient_id),
            new_medical_record
        )
    except HTTPException as e:
        return APIResponse.as_json(code=e.status_code, message=str(e.detail))
    return APIResponse.as_json(
        code=status.HTTP_200_OK,
        data=new_medical_record,
        message="Medical record updated successfully"
    )

@router.delete("/{medical_record_id}", tags=["medial_record"], response_model=MedicalRecordResponseModel)
async def delete_medical_record(
    medical_record_id: int,
    service: MedicalRecordService = Depends(MedicalRecordService)
):
    try:
        medical_record = await service.delete(
            QueryMedicalRecordModel(id=medical_record_id)
        )
    except HTTPException as e:
        return APIResponse.as_json(code=e.status_code, message=str(e.detail))
    return APIResponse.as_json(
        code=status.HTTP_200_OK,
        data=medical_record,
        message="Medical record deleted successfully"
    )
