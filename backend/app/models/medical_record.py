from pydantic import BaseModel
from models.response import BaseResponseModel
from typing import Optional


class QueryMedicalRecordModel(BaseModel):
    patient_id: Optional[str]
    id: Optional[str]

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
    current_treatment: Optional[str]
    drug_allergies: Optional[str]
    food_allergies: Optional[str]
    medical_history: Optional[str]
    progress: Optional[list[Optional[ProgressRecordModel]]]


class NewMedicalRecordModel(BaseModel):
    patient_id: str
    weight: float
    height: float
    note: Optional[str]
    current_treatment: Optional[str]
    drug_allergies: Optional[str]
    food_allergies: Optional[str]
    medical_history: Optional[str]
    
class PatchMedicalRecordModel(BaseModel):
    weight: Optional[float]
    height: Optional[float]
    note: Optional[str]
    current_treatment: Optional[str]
    drug_allergies: Optional[str]
    food_allergies: Optional[str]
    medical_history: Optional[str]


class DeleteMedicalRecordModel(BaseModel):
    id: Optional[str]
    patient_id: Optional[str]

class MedicalRecordResponseModel(BaseResponseModel):
    data: MedicalRecordModel
