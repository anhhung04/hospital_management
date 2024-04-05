from fastapi import APIRouter, Depends, status, HTTPException, Query
from services.patient import PatientService
from typing import Annotated
from util.response import APIResponse
from models.patient import (
    ListPatientsModel, AddPatientRequestModel, NewPatientReponseModel,
    PatientDetailResponseModel, QueryPatientModel, PatchPatientModel
)
from models.patient_progress import NewPatientProgressModel, QueryPatientProgressModel, PatientProgressResponseModel
from models.request import IdPath

router = APIRouter()


@router.get("/list", response_model=ListPatientsModel, tags=["patient"])
async def list_patients(
    page: Annotated[int, Query(gt=0)] = 1,
    limit: Annotated[int, Query(gt=0)] = 10,
    service: PatientService = Depends(PatientService),
):
    try:
        patients = await service.get_patients(
            page, limit
        )
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code, message=str(e.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, data=patients, message="Patients fetched successfully"
    )


@router.get("/{patient_id}", tags=["patient"], response_model=PatientDetailResponseModel)
async def get_patient(
    patient_id: IdPath,
    max_progress: int = Query(lt=10, gt=0, default=1),
    service: PatientService = Depends(PatientService),
):
    try:
        patient = await service.get(
            QueryPatientModel(
                user_id=patient_id,
                max_progress=max_progress
            )
        )
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code, message=str(e.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, data=patient, message="Patient fetched successfully"
    )


@router.post("/create", tags=["patient"], response_model=NewPatientReponseModel)
async def create_patient(
    patient: AddPatientRequestModel,
    service: PatientService = Depends(PatientService),
):
    try:
        patient = await service.create(patient)
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code, message=str(e.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, data=patient, message="Patient created successfully"
    )


@router.patch("/{patient_id}/update", tags=["patient"], response_model=PatientDetailResponseModel)
async def patch_patient(
    patient_id: IdPath,
    patient_update: PatchPatientModel,
    service: PatientService = Depends(PatientService),
):
    try:
        patient = await service.update(
            QueryPatientModel(user_id=patient_id),
            patient_update
        )
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code, message=str(e.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, data=patient, message="Patient updated successfully"
    )


@router.post(
    "/{patient_id}/progress/create",
    tags=["patient"],
    response_model=PatientProgressResponseModel
)
async def add_new_patient_progress(
    patient_id: IdPath,
    progress: NewPatientProgressModel,
    service: PatientService = Depends(PatientService),
):
    try:
        new_progress = await service.add_progress(
            QueryPatientProgressModel(patient_id=patient_id),
            progress
        )
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code, message=str(e.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK,
        data=new_progress,
        message="Progress added successfully"
    )
