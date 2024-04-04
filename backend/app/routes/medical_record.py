from fastapi import APIRouter, Request, Depends, HTTPException, status
from repository import Storage
from models.medical_record import (
    MedicalRecordResponseModel, NewMedicalRecordModel, QueryMedicalRecordModel, PatchMedicalRecordModel
)
from services.medical_record import MedicalRecordService
from util.response import APIResponse

router = APIRouter()


@router.get("/{patient_id}", tags=["medial_record"], response_model=MedicalRecordResponseModel)
async def get_medicalrecord(
    request: Request,
    patient_id: str,
    db=Depends(Storage.get),
):
    try:
        medical_record = await MedicalRecordService(db, request.state.user).get(
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
    request: Request,
    db=Depends(Storage.get),
):
    try:
        medical_record = await MedicalRecordService(db, request.state.user).get_me()
    except HTTPException as e:
        return APIResponse.as_json(code=e.status_code, message=str(e.detail))
    return APIResponse.as_json(
        code=status.HTTP_200_OK,
        data=medical_record,
        message="Medical record fetched successfully"
    )


@router.post("/create", tags=["medial_record"], response_model=MedicalRecordResponseModel)
async def create_new_medical_record(
    request: Request,
    medical_record: NewMedicalRecordModel,
    db=Depends(Storage.get),
):
    try:
        medical_record = await MedicalRecordService(db, request.state.user).create(
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
    request: Request,
    patient_id: str,
    new_medical_record: PatchMedicalRecordModel,
    db=Depends(Storage.get),
):
    try:
        new_medical_record = await MedicalRecordService(db, request.state.user).update(
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
    request: Request,
    medical_record_id: int,
    db=Depends(Storage.get),
):
    try:
        medical_record = await MedicalRecordService(db, request.state.user).delete(
            QueryMedicalRecordModel(id=medical_record_id)
        )
    except HTTPException as e:
        return APIResponse.as_json(code=e.status_code, message=str(e.detail))
    return APIResponse.as_json(
        code=status.HTTP_200_OK,
        data=medical_record,
        message="Medical record deleted successfully"
    )
