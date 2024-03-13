from datetime import datetime
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from interface.serviceable import Serviceable


class Palindrome(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()