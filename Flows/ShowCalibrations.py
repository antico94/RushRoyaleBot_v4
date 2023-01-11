import asyncio
import collections
import concurrent.futures
import time

import cv2

from Utils.GameTools import SetTilesBoxes, CreateBoard, GuessUnit
from Utils.ImageTools import CropImage, ConvertImageToNumpyArray, DrawContour
from Utils.OSTools import GetAllSubdirectoriesFromFolder
from Utils.ScreenTools import GetScreenshot, GetAppWindow, GetOwnUnitsWindow
from Utils.WrapperTools import MeasurePerformance

# GLOBAL VARIABLES
#############################################################
TEST_DIR = 'C:/Users/Meiu/Desktop/short_unit_np'
CLASS_LABELS = GetAllSubdirectoriesFromFolder(TEST_DIR)
APP_WINDOW = GetAppWindow()
UNITS_WINDOW = GetOwnUnitsWindow(APP_WINDOW)
BOARD = CreateBoard()
SetTilesBoxes(board=BOARD, ownUnitsWindow=UNITS_WINDOW)
TILES = BOARD.GetAllTiles()
#############################################################

loop = asyncio.get_event_loop()


@MeasurePerformance
async def ShowCalibrations():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        start_time = time.time()
        num_frames = 0
        while True:
            # time.sleep(1)
            image = await loop.run_in_executor(executor, GetScreenshot, UNITS_WINDOW)
            tasks = collections.deque()
            for tile in TILES:
                window = tile.window
                task = loop.run_in_executor(executor, CropImage, ConvertImageToNumpyArray(image), window)
                tasks.append(task)
            done, pending = await asyncio.wait(tasks)
            results = [task.result() for task in done]
            tasks = []
            for i, tile in enumerate(TILES):
                task = loop.run_in_executor(executor, GuessUnit, results[i], CLASS_LABELS)
                tasks.append(task)
            done, pending = await asyncio.wait(tasks)
            guesses = [task.result() for task in done]
            for i, tile in enumerate(TILES):
                image = DrawContour(ConvertImageToNumpyArray(image), tile.window, guesses[i])
            image = cv2.resize(image, (0, 0), fx=2, fy=2)
            cv2.imshow("Screenshot", image)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            num_frames += 1
            elapsed_time = time.time() - start_time
            if elapsed_time > 1:
                fps = num_frames / elapsed_time
                print("FPS:", fps)
                start_time = time.time()
                num_frames = 0


loop.run_until_complete(ShowCalibrations())
