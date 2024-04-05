from pydantic import BaseModel, validator
from models.response import BaseResponseModel
from typing import Optional
from datetime import datetime

class ProgressRecordModel(BaseModel):
    id: int
    created_at: str
    treatment_schedule: str
    treatment_type: str
    patient_condition: str

    @validator('created_at', pre=True)
    def validate_created_at(cls, v):
        if v and isinstance(v, datetime):
            return v.strftime('%Y-%m-%d %H:%M:%S')
        return str(v)


class MedicalRecordModel(BaseModel):
    id: int
    weight: Optional[float | None]
    height: Optional[float | None]
    note: Optional[str]
    current_treatment: Optional[str | None]
    drug_allergies: Optional[str | None]
    food_allergies: Optional[str | None]
    medical_history: Optional[str | None]
    progress: Optional[list[Optional[ProgressRecordModel | None]] | None] = None


class NewMedicalRecordModel(BaseModel):
    weight: Optional[float | None] = None
    height: Optional[float | None] = None
    note: Optional[str | None] = None
    current_treatment: Optional[str | None] = None
    drug_allergies: Optional[str | None] = None
    food_allergies: Optional[str | None] = None
    medical_history: Optional[str | None] = None
    
class PatchMedicalRecordModel(BaseModel):
    weight: Optional[float | None] = None
    height: Optional[float | None] = None
    note: Optional[str | None] = None
    current_treatment: Optional[str | None] = None
    drug_allergies: Optional[str | None] = None
    food_allergies: Optional[str | None] = None
    medical_history: Optional[str | None] = None


class DeleteMedicalRecordModel(BaseModel):
    id: Optional[int | None] = None
    patient_id: Optional[str | None] = None

class MedicalRecordResponseModel(BaseResponseModel):
    data: MedicalRecordModel


class QueryMedicalRecordModel(BaseModel):
    id: Optional[int | None] = None
    patient_id: Optional[str | None] = None
