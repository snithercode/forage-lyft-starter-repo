from typing import List
from interface.serviceable import Serviceable

class CarriganTires(Serviceable):
    def __init__(self, tire_wear: List[int]):
        self.tire_wear = tire_wear
    
    def needs_service(self) -> bool:
        for tire_wear_value in self.tire_wear:
            if tire_wear_value >= 0.9:
                return True
        return False
