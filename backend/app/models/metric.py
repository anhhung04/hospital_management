from models.response import BaseResponseModel
from pydantic import BaseModel


class MetricModel(BaseModel):
    num_patients: int
    num_doctors: int
    num_nurses: int
    num_managers: int
    num_other: int
    num_employee: int
    patients_per_day: list[int]


class MetricResponseModel(BaseResponseModel):
    data: MetricModel
