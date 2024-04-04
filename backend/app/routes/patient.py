from fastapi import APIRouter, Depends
from services.patient import PatientService
from fastapi import Query, status, HTTPException, Path
from typing import Annotated
from util.response import APIResponse
from models.patient import (
    ListPatientsModel, AddPatientRequestModel, NewPatientReponseModel,
    PatientDetailResponseModel, QueryPatientModel, PatchPatientModel
)

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
    patient_id: Annotated[str, Path(regex=r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")],
    service: PatientService = Depends(PatientService),
):
    try:
        patient = await service.get(
            QueryPatientModel(user_id=patient_id)
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


@router.patch("/update/{patient_id}", tags=["patient"], response_model=PatientDetailResponseModel)
async def patch_patient(
    patient_id: Annotated[str, Path(regex=r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")],
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
