from pydantic import BaseModel, validator
from typing import Optional
from models.response import BaseResponseModel
from repository.schemas.patient import ProgressType
from datetime import datetime


class ProgressRecordModel(BaseModel):
    id: int
    created_at: str
    patient_condition: str
    start_treatment: str
    end_treatment: str
    status: Optional[str | None] = None

    @validator('created_at', pre=True)
    def validate_created_at(cls, v):
        if v and isinstance(v, datetime):
            return v.strftime('%Y-%m-%d %H:%M:%S')
        return str(v)

    @validator('start_treatment', pre=True)
    def validate_start_treatment(cls, v):
        if v and isinstance(v, datetime):
            return v.strftime('%Y-%m-%d %H:%M:%S')
        return str(v)

    @validator('end_treatment', pre=True)
    def validate_end_treatment(cls, v):
        if v and isinstance(v, datetime):
            return v.strftime('%Y-%m-%d %H:%M:%S')
        return str(v)


class NewPatientProgressModel(BaseModel):
    start_treatment: str
    end_treatment: str
    status: Optional[ProgressType | None] = None
    patient_condition: Optional[str | None] = None

class PatientProgressResponseModel(BaseResponseModel):
    data: ProgressRecordModel


class QueryPatientProgressModel(BaseModel):
    patient_id: Optional[str | None] = None
    max_progress: Optional[int | None] = None
    progress_id: Optional[int | None] = None
    status: Optional[str | None] = None
