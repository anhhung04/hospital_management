from pydantic import BaseModel
from models.response import BaseResponseModel
from repository.schemas.user import ObjectID


class PatientResponseMode(BaseModel):
    id: ObjectID
    full_name: str
    phone_number: str
    medical_record: ObjectID

class ListPatientsModel(BaseResponseModel):
    data: list[PatientResponseMode]
