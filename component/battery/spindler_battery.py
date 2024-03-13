from datetime import date
from interface.serviceable import Serviceable

class SpindlerBattery(Serviceable):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    def needs_service(self) -> bool:
        return (datetime.now().year - self.last_service_date.year) > 2