from pydantic import BaseModel, validator
from typing import Optional
from models.response import BaseResponseModel
from datetime import datetime


class NewPatientProgressModel(BaseModel):
    treatment_schedule: Optional[str | None] = None
    duration: Optional[int | None] = None
    treatment_type: Optional[str | None] = None
    patient_condition: Optional[str | None] = None


class PatientProgressModel(NewPatientProgressModel):
    id: int
    created_at: str

    @validator('created_at', pre=True)
    def validate_created_at(cls, v):
        if v and isinstance(v, datetime):
            return v.strftime('%Y-%m-%d %H:%M:%S')
        return str(v)


class PatientProgressResponseModel(BaseResponseModel):
    data: PatientProgressModel


class QueryPatientProgressModel(BaseModel):
    patient_id: Optional[str | None] = None
    max_progress: Optional[int | None] = None
    progress_id: Optional[int | None] = None
    status: Optional[str | None] = None
