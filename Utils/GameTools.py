import cv2
import numpy as np
import tensorflow as tf

from Classes.Board import Board
from Classes.Box import Box
from Classes.Buff import Buff
from Classes.Tile import Tile
from Utils.ScreenTools import ShowCapture


def ConvertIndexToCoordinate(index):
    return str(chr(index // 3 + 65)) + str(index % 3 + 1)


def CreateEmptyTile():
    box = Box(0, 0, 0, 0)
    return Tile(coordinates='', window=box, buffs=Buff(), debuff=False, hasUnit=False, currentUnit=None)


def CreateBoard():
    rows = [1, 2, 3]
    columns = ["A", "B", "C", "D", "E"]
    board = Board()
    for column in columns:
        for row in rows:
            board.__setattr__(f'{column}{row}', CreateEmptyTile())
    return board


# @CheckArguments
def SetTilesBoxes(ownUnitsWindow: Box, board: Board):
    tileWidth = int(ownUnitsWindow.width / 5)
    tileHeight = int(ownUnitsWindow.height / 3)
    currentStartWidth = 0
    currentStartHeight = 0
    tiles = board.GetAllTiles()
    for index, tile in enumerate(tiles):
        unitBox = Box(left=currentStartWidth, top=currentStartHeight, width=currentStartWidth + tileWidth,
                      height=currentStartHeight + tileHeight)
        tile.window = unitBox
        tile.coordinates = ConvertIndexToCoordinate(index)
        board.__setattr__(f'{tile.coordinates}', tile)
        currentStartHeight += tileHeight
        if (index - 2) % 3 == 0:
            currentStartHeight = 0
            currentStartWidth += tileWidth
    return 'Done'


class ClassifyPillowImage:
    pass


def GuessUnit(image, classlist):
    model = tf.keras.models.load_model('C:\\Users\\Meiu\\Desktop\\RushRoyaleBot_v4\\Neural Network\\GeneratedModels\\units_model_np.h5')
    image = image.astype(np.float32)
    image = image.reshape((-1, 55, 57, 3))
    prediction = model.predict(image)
    index = np.argmax(prediction)
    # Return the predicted unit
    return classlist[index]

