from datetime import date
from interface.serviceable import Serviceable


class CapuletEngine(Serviceable):
    def __init__(self, current_mileage: int, last_service_mileage: int, last_service_date: date):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.last_service_date = last_service_date

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 30000
