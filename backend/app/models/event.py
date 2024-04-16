from pydantic import BaseModel, ConfigDict
from dateutil.rrule import(
    MO, TU, WE, TH, FR, SA, SU,
    DAILY, WEEKLY, MONTHLY, YEARLY
)
from repository.schemas.employees import Frequency, DayOfWeek 
from datetime import date
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
    
    id: int
    title: str
    begin_date: str
    end_date: str
    day_of_week: DayOfWeek
    begin_time: str
    end_time: str
    occurence: list[str]

class ListEventResponseModel(BaseModel):
    data: list[ListEventModel]

class EventModel(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    id: int
    title: str
    begin_date: str
    end_date: str
    day_of_week: DayOfWeek
    begin_time: str
    end_time: str

class EventReponseModel(BaseModel):
    data: EventModel

class EventRequestModel(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    title: str
    day_of_week: DayOfWeek
    begin_time: str
    end_time: str
    begin_date: str
    end_date: str
    is_recurring: bool
    frequency: Frequency

class PatchEventRequestModel(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    title: Optional[str | None] = None
    begin_time: Optional[str | None] = None
    end_time: Optional[str | None] = None
    end_date: Optional[str | None] = None
    is_recurring: Optional[bool | None] = None
    frequency: Optional[Frequency | None] = None