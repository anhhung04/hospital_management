from fastapi import APIRouter, Depends, Request
from services.patient import PatientService
from repository import Storage
from fastapi import Query, status, HTTPException, Path
from typing import Annotated
from util.response import APIResponse
from models.patient import ListPatientsModel, AddPatientRequestModel, NewPatientReponseModel, PatientResponseModel, NewPatientRequestModel, PatientDetailResponseModel

router = APIRouter()


@router.get("/list", response_model=ListPatientsModel, tags=["patient"])
async def list_patients(
    request: Request,
    page: Annotated[int, Query(gt=0)] = 1,
    patient_per_page: Annotated[int, Query(gt=0)] = 10,
    db_sess=Depends(Storage.get),
):
    try:
        patients = PatientService(db_sess, request.state.user).get_patients(
            page, patient_per_page)
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code, message=str(e.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, data=patients, message="Patients fetched successfully"
    )


@router.get("/{patient_id}", tags=["patient"], response_model=PatientDetailResponseModel)
async def get_patient(
    request: Request,
    patient_id: Annotated[str, Path(regex=r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")],
    db_sess=Depends(Storage.get),
):
    try:
        patient = PatientService(db_sess, request.state.user).get(patient_id)
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code, message=str(e.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, data=patient, message="Patient fetched successfully"
    )


@router.post("/create", tags=["patient"], response_model=NewPatientReponseModel)
async def create_patient(
    user_info: AddPatientRequestModel,
    request: Request,
    db_sess=Depends(Storage.get)
):
    try:
        patient = PatientService(db_sess, request.state.user).create(user_info)
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
    request: Request,
    patient_update: NewPatientRequestModel,
    db_sess=Depends(Storage.get),
):
    try:
        patient = PatientService(
            db_sess, request.state.user).update(patient_id, patient_update)
    except HTTPException as e:
        return APIResponse.as_json(
            code=e.status_code, message=str(e.detail), data={}
        )
    return APIResponse.as_json(
        code=status.HTTP_200_OK, data=patient, message="Patient updated successfully"
    )
