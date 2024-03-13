from interface.serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery
    
    def needs_service(self) -> bool:
        raise NotImplementedError("Subclasses must implement abstract method")
