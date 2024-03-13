from datetime import datetime
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from interface.serviceable import Serviceable


class Rorschach(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()