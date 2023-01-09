from typing import List

from Classes.UnitCalibration import UnitCalibration


class Unit:
    def __init__(self, name: str, colorList: List[UnitCalibration]):
        self.name = name
        self.colorList = colorList

    def to_json(self):
        # Return a dictionary representing the state of the object
        return {
            'name': self.name,
            'colorList': [c.to_json() for c in self.colorList]
        }
