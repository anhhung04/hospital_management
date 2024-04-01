from fastapi import APIRouter, Depends
from util.jwt import JWTHandler
from services.patient import PatientService
from repository import Storage

router = APIRouter()


@router.get("/patient", dependencies=[Depends(JWTHandler.verify_auth_header)])
async def list_patients(db_sess=Depends(Storage.get)):
    patients = PatientService(db_sess).get_patients(
        page=1, patient_per_page=10)
    return patients
