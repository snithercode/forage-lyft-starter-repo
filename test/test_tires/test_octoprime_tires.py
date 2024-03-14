import unittest

from component.tires.octoprime_tires import OctoprimeTires

class TestCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.8, 0.8, 0.8, 0.8]
        tires = OctoprimeTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.5, 0.5, 0.5, 0.5]
        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service())