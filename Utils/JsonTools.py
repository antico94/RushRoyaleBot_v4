import json
import os

from Classes.Unit import Unit
from Logger.Logger import logger


def IsPropertyPresent(jsonFile, propertyName, propertyValue):
    logger.info("Checking if file exists and is not empty")
    if os.stat(jsonFile).st_size != 0:
        logger.info("File exists and is not empty")
        with open(jsonFile) as f:
            data = json.load(f)
            logger.info("Loaded data from file")
            for obj in data:
                if obj[propertyName] == propertyValue:
                    logger.info("Property found")
                    return True
            logger.info("Property not found")
            return False
    logger.info("File does not exist or is empty")
    return False


def GetObjectFromJson(file_path, propertyName, propertyValue):
    with open(file_path, 'r') as f:
        data = json.load(f)
        for obj in data:
            if obj[propertyName] == propertyValue:
                return obj


def SaveUnitToJson(file_path, unit):
    # Check if file exists
    if os.path.exists(file_path):
        # Open file in read mode
        with open(file_path, 'r') as f:
            # Load json data from file
            try:
                units_data = json.load(f)
            except json.decoder.JSONDecodeError:
                # If the file is empty, create an empty list
                units_data = []
    else:
        # If the file does not exist, create an empty list
        units_data = []

    # Append the data to the list
    units_data.append(unit.to_json())

    # Open file in write mode
    with open(file_path, 'w') as f:
        # Write the list to the file
        json.dump(units_data, f)


def ImportUnitsCalibrations():
    with open('../json/units.json', 'r') as f:
        json_data = f.read()
        data = json.loads(json_data)

        objectList = []
        for item in data:
            obj = Unit(
                name=item['name'],
                colorList=item['colorList'],
            )
            objectList.append(obj)
    return objectList
