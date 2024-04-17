from pydantic import BaseModel, ConfigDict, validator
from dateutil.rrule import(
    MO, TU, WE, TH, FR, SA, SU,
    DAILY, WEEKLY, MONTHLY, YEARLY
)
from repository.schemas.employees import Frequency, DayOfWeek 
from typing import Optional
from datetime import datetime

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
    frequency: Frequency
    occurence: list[str]

    @validator('occurence')
    def get_occurence(cls, v, values):
        is_recurring_value = values.get('is_recurring')
        if is_recurring_value and len(v) >= 1:
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
    frequency: Frequency

class EventReponseModel(BaseModel):
    data: EventModel

class EventRequestModel(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    title: str
    day_of_week: DayOfWeek
    begin_time: str
    end_time: str
    begin_date: str
    is_recurring: bool = False
    end_date: Optional[str | None] = None
    frequency: Frequency = Frequency.SINGLE

    @validator('frequency')
    def required_frequency_if_is_recurring(cls, v, values):
        is_recurring_value = values.get('is_recurring')
        if is_recurring_value and v != Frequency.SINGLE.value:
            return v
        elif not is_recurring_value and v == Frequency.SINGLE.value:
            return v
        raise ValueError("Frequency and is_recurring value mismatched")
    
    @validator('end_date', pre=False)
    def required_end_date_if_recurring(cls, v, values):
        is_recurring_value = values.get('is_recurring')
        print(is_recurring_value)
        if is_recurring_value:
            return v
        if v is None:
            return values.get('begin_date')
        return v
    
    @validator('end_time')
    def match_begin_and_end_time(cls, v, values):
        begin_time = values.get('begin_time')
        time_format = "%H:%M:%S"
        begin = datetime.strptime(begin_time, time_format).time()
        end = datetime.strptime(v, time_format).time()
        if begin < end:
            return v
        raise ValueError("End time must be greater than begin time")
    
class AddEventModel(EventRequestModel):
    id: str

class PatchEventRequestModel(BaseModel):
    model_config = ConfigDict(use_enum_values=True)

    title: Optional[str | None] = None
    begin_time: Optional[str | None] = None
    end_time: Optional[str | None] = None
    end_date: Optional[str | None] = None

    @validator('end_time')
    def match_begin_and_end_time(cls, v, values):
        begin_time = values.get('begin_time')
        if begin_time and v:
            time_format = "%H:%M:%S"
            begin = datetime.strptime(begin_time, time_format).time()
            end = datetime.strptime(v, time_format).time()
            if begin < end:
                return v
            raise ValueError("End time must be greater than begin time")