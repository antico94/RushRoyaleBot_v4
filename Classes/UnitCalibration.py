class UnitCalibration:
    def __init__(self, rgbValues=None, concentration=0):
        if rgbValues is None:
            rgbValues = []
        self.rgbValues = rgbValues
        self.concentration = concentration

    def ImportValuesFromJson(self, jsonObject):
        self.rgbValues = jsonObject['colors']
        self.concentration = jsonObject['concentration']
        return self

    def to_json(self):
        # Return a dictionary representing the state of the object
        return {
            'rgbValues': self.rgbValues,
            'concentration': self.concentration
        }
