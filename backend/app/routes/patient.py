from fastapi import APIRouter, Depends, Request, HTTPException
from services.patient import PatientService
from repository import Storage
from fastapi import Query
from typing import Annotated

router = APIRouter()


@router.get("/patient")
async def list_patients(
    request: Request,
    page=Annotated[int, Query(gt=0)],
    patient_per_page=Annotated[int, Query(gt=0)],
    db_sess=Depends(Storage.get)
):
    if not request.state.user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    if request.state.user.role == 'EMPLOYEE':
        raise HTTPException(status_code=403, detail="Forbidden")    
    patients = PatientService(db_sess).get_patients(page, patient_per_page)
    return patients
