from datetime import date
from typing import List
from car import Car
from component.engine.capulet_engine import CapuletEngine
from component.engine.willoughby_engine import WilloughbyEngine
from component.engine.sternman_engine import SternmanEngine
from component.battery.spindler_battery import SpindlerBattery
from component.battery.nubbin_battery import NubbinBattery
from component.tires.carrigan_tires import CarriganTires
from component.tires.octoprime_tires import OctoprimeTires


class CarFactory:
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: List[float]) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        tires = CarriganTires(tire_wear)
        car = Car(engine, battery, tires)
        return car

    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: List[float]) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        tires = OctoprimeTires(tire_wear)
        car = Car(engine, battery, tires)
        return car

    def create_palindrome(current_date: date, last_service_date: date, warning_light_is_on: bool, tire_wear: List[float]) -> Car:
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date)
        tires = CarriganTires(tire_wear)
        car = Car(engine, battery, tires)
        return car

    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: List[float]) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        tires = OctoprimeTires(tire_wear)
        car = Car(engine, battery, tires)
        return car

    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: List[float]) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        car = Car(engine, battery, tires)
        return car