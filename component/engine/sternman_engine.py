from interface.serviceable import Serviceable

class SternmanEngine(Serviceable):
    def __init__(self, warning_light_is_on: bool):
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self) -> bool:
        return self.warning_light_is_on
