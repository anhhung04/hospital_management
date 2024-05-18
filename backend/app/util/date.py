from datetime import date, datetime, timedelta

class DateProcessor:
    
    @staticmethod
    def get_current_date() -> str:
        return date.today().strftime("%Y-%m-%d")

    @staticmethod
    def get_current_time() -> str:
        return datetime.now().strftime("%H:%M:%S")

    @staticmethod
    def get_current_datetime() -> str:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @staticmethod
    def get_day_of_week(date: str) -> str:
        week = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
        date = datetime.strptime(date, "%Y-%m-%d")
        days_to_monday = date.weekday()
        return week[days_to_monday]
    
    @staticmethod
    def handle_param_date(begin_date: date | None, end_date: date | None) -> tuple[date, date]:
        if not begin_date:
            current_date = datetime.now().date()
            days_to_monday = current_date.weekday()
            begin_date = current_date - timedelta(days=days_to_monday)
            end_date = begin_date + timedelta(days=6)
        if not end_date:
            end_date = begin_date + timedelta(days=6)
        return begin_date, end_date