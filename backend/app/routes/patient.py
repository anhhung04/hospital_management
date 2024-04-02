from fastapi import APIRouter, Depends
from services.patient import PatientService
from repository import Storage
from fastapi import Query
from typing import Annotated
from middleware.user_ctx import get_current_user

router = APIRouter()


@router.get("/patient")
async def list_patients(
    page=Annotated[int, Query(gt=0)],
    patient_per_page=Annotated[int, Query(gt=0)],
    db_sess=Depends(Storage.get),
    user=Depends(get_current_user)
):
    patients = PatientService(db_sess, user).get_patients(
        page, patient_per_page, user)
    return patients
