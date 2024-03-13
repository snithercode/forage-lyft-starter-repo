from abc import ABC

from car import Car


class WilloughbyEngine(Serviceable):
    def __init__(self, last_service_date, current_mileage: int, last_service_mileage: int, last_service_date: int):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.last_service_date = last_service_date

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 60000
