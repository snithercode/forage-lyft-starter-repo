from datetime import date

from interface.serviceable import Serviceable

class SpindlerBattery(Serviceable):
    def __init__(self, current_date: date, last_service_date: date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self) -> bool:
        years_since_last_service = self.current_date.year - self.last_service_date.year
        return years_since_last_service >= 2