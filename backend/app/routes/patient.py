from fastapi import APIRouter, Depends, Request
from services.patient import PatientService
from repository import Storage
from fastapi import Query, status, HTTPException
from typing import Annotated
from util.response import APIResponse
from models.patient import ListPatientsModel

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
