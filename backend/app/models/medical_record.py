from pydantic import BaseModel
from models.response import BaseResponseModel
from typing import Optional

class ProgressRecordModel(BaseModel):
    id: str
    created_at: int
    treatment_schedule: int
    treatment_type: str
    patient_condition: str


class MedicalRecordModel(BaseModel):
    id: str
    patient_id: str
    weight: float
    height: float
    note: Optional[str]
    current_treatment: Optional[str | None]
    drug_allergies: Optional[str | None]
    food_allergies: Optional[str | None]
    medical_history: Optional[str | None]
    progress: Optional[list[Optional[ProgressRecordModel]]]


class NewMedicalRecordModel(BaseModel):
    patient_id: str
    weight: float
    height: float
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
    id: Optional[str | None] = None
    patient_id: Optional[str | None] = None

class MedicalRecordResponseModel(BaseResponseModel):
    data: MedicalRecordModel


class QueryMedicalRecordModel(BaseModel):
    patient_id: Optional[str | None] = None
    id: Optional[int | None] = None
