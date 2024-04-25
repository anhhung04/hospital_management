from models.response import BaseResponseModel
from pydantic import BaseModel


class MetricModel(BaseModel):
    num_patients: int
    num_doctors: int
    num_employee: int
    patients_per_day: list[int]


class MetricResponseModel(BaseResponseModel):
    data: MetricModel
