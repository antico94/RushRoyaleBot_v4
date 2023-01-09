import json
from typing import Union

from Classes.Box import Box
from Classes.Unit import Unit


class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


class Tile:
    def __init__(self, coordinates: str, window: Box, buffs, debuff, hasUnit: bool, currentUnit: Union[None, Unit]):
        self.coordinates = coordinates
        self.window = window
        self.buffs = buffs
        self.debuff = debuff
        self.hasUnit = hasUnit
        self.currentUnit = currentUnit
