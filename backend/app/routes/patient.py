from fastapi import APIRouter, Depends
from services.patient import PatientService
from repository import Storage
from fastapi import Query
from typing import Annotated

router = APIRouter()


@router.get("/patient")
async def list_patients(
    page=Annotated[int, Query(gt=0)],
    patient_per_page=Annotated[int, Query(gt=0)],
    db_sess=Depends(Storage.get)
):
    patients = PatientService(db_sess).get_patients(page, patient_per_page)
    return patients
