import concurrent.futures
import math
import sys
import uuid

import cv2

from Utils.GameTools import SetTilesBoxes, CreateBoard
from Utils.ImageTools import CropImage, ConvertImageToNumpyArray
from Utils.ScreenTools import GetScreenshot, GetAppWindow, GetOwnUnitsWindow


def SaveImage(image, unit_name):
    file_name = str(uuid.uuid4()) + '.png'
    file_path = f'C:\\Users\\Meiu\\Desktop\\unit\\{unit_name}\\{file_name}'
    # Save the image to the file path
    cv2.imwrite(file_path, image)


def DownloadImage(unitsWindow, tile, unit_name):
    window = tile.window
    cropped_image = CropImage(ConvertImageToNumpyArray(GetScreenshot(unitsWindow)), window)
    SaveImage(cropped_image, unit_name)


def ShowCalibrations():
    appWindow = GetAppWindow()
    unitsWindow = GetOwnUnitsWindow(appWindow)
    board = CreateBoard()
    SetTilesBoxes(board=board, ownUnitsWindow=unitsWindow)

    counter = 0
    total_photos = 1000
    interest = ['A1', 'A2', 'A3', 'B1', 'B3', 'C1', 'C2', 'C3', 'D1', 'D2', 'D3', 'E1', 'E2', 'E3']
    interest = ['B1', 'D1', 'E1', 'A2']
    unit_name = 'Sword'
    while counter < total_photos:
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            # submit a task to download each image in the interest list
            futures = [executor.submit(DownloadImage, unitsWindow, tile, unit_name) for tile in board.GetAllTiles() if
                       tile.coordinates in interest]

            # count the number of completed tasks
            counter += len([future for future in concurrent.futures.as_completed(futures)])

            # print progress bar
            progress = counter / total_photos
            sys.stdout.write('\r[{:<{}}] {:.0f}%'.format('#' * int(math.ceil(progress * 20)), 20, progress * 100))


ShowCalibrations()
