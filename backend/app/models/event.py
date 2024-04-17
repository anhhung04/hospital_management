from pydantic import BaseModel, ConfigDict, validator
from dateutil.rrule import(
    MO, TU, WE, TH, FR, SA, SU,
    DAILY, WEEKLY, MONTHLY, YEARLY
)
from repository.schemas.employees import Frequency, DayOfWeek 
from typing import Optional

day_of_week_map = {
  "MONDAY": MO,
  "TUESDAY": TU,
  "WEDNESDAY": WE,
  "THURSDAY": TH,
  "FRIDAY": FR,
  "SATURDAY": SA,
  "SUNDAY": SU
}

freq_map = {
  "DAILY": DAILY,
  "WEEKLY": WEEKLY,
  "MONTHLY": MONTHLY,
  "YEARLY": YEARLY
}

class ListEventModel(BaseModel):
    model_config = ConfigDict(use_enum_values=True)
    
    id: str
    title: str
    begin_date: str
    end_date: Optional[str | None] = None
    day_of_week: DayOfWeek
    begin_time: str
    end_time: str
    is_recurring: bool = False
    occurence: list[str]

    @validator('occurence')
    def get_occurence(cls, v, values):
        is_recurring_value = values.get('is_recurring')
        if is_recurring_value and len(v) > 1:
            return v
        elif not is_recurring_value and len(v) == 1:
            return v
        raise ValueError("Occurence and is_recurring value mismatched")

class ListEventResponseModel(BaseModel):
    data: list[ListEventModel]

class EventModel(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: str
    title: str
    begin_date: str
    end_date: Optional[str | None] = None
    day_of_week: DayOfWeek
    begin_time: str
    end_time: str
    is_recurring: bool
    frequency: Optional[Frequency | None] = None

class EventReponseModel(BaseModel):
    data: EventModel

class EventRequestModel(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    title: str
    day_of_week: DayOfWeek
    begin_time: str
    end_time: str
    begin_date: str
    end_date: Optional[str | None] = None
    is_recurring: bool = False
    frequency: Optional[Frequency | None] = None

    @validator('frequency')
    def required_frequency_if_recurring(cls, v, values):
        is_recurring_value = values.get('is_recurring')
        if is_recurring_value and v is not None:
            return v
        elif not is_recurring_value and v is None:
            return v
        raise ValueError("Frequency is required for recurring events")
    
class AddEventModel(EventRequestModel):
    id: str

class PatchEventRequestModel(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    title: Optional[str | None] = None
    begin_time: Optional[str | None] = None
    end_time: Optional[str | None] = None
    end_date: Optional[str | None] = None
    is_recurring: Optional[bool | None] = None
    frequency: Optional[Frequency | None] = None

    # @validator('frequency')
    # def required_frequency_if_recurring(cls, v, values):
    #     if values.get('is_recurring') and v is None:
    #         raise ValueError("Frequency is required for recurring events")
    #     return v