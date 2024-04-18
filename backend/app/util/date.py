from datetime import date, datetime

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