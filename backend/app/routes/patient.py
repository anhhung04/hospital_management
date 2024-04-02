from fastapi import APIRouter, Depends
from services.patient import PatientService
from repository import Storage
from fastapi import Query, status
from typing import Annotated
from middleware.user_ctx import get_current_user
from util.response import APIResponse

router = APIRouter()


@router.get("/")
async def list_patients(
    page=Annotated[int, Query(gt=0, default=1)],
    patient_per_page=Annotated[int, Query(gt=0, default=10)],
    db_sess=Depends(Storage.get),
    user=Depends(get_current_user)
):
    patients = PatientService(db_sess, user).get_patients(
        page, patient_per_page, user)
    return APIResponse.as_json(
        code=status.HTTP_200_OK, data=patients, message="Patients fetched successfully"
    )
