from pydantic import BaseModel
from typing import Optional


class PatientProgressModel(BaseModel):
    id: int
    created_at: str
    treatment_schedule: Optional[str | None] = None
    duration: Optional[int | None] = None
    treatment_type: Optional[str | None] = None
    patient_condition: Optional[str | None] = None
    status: str
