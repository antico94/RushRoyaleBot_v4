import time

import cv2
import numpy as np
import pyautogui
import win32con
import win32gui
from PIL import ImageOps

from Utils.WrapperTools import CheckArguments
from Classes.Box import Box

# GLOBAL CONSTANTS
###################################################################################

# LOCATE WINDOW IMAGES
BOTTOM_RIGHT_CORNER_IMAGE = 'assets/screen_guidance/bottom_right_corner.png'
TOP_LEFT_CORNER_IMAGE = 'assets/screen_guidance/left_top_corner.png'

# LOCATE UNITS IMAGES
BOTTOM_BORDER_UNITS_IMAGE = 'assets/screen_guidance/bottom_border_units.png'
TOP_BORDER_UNITS_IMAGE = 'assets/screen_guidance/top_border_units.png'


###################################################################################

# @CheckArguments
def ShowCapture(img: np.ndarray):
    cv2.imshow('test', img)
    while 1:
        if cv2.waitKey(25) * 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


# @CheckArguments
def GetScreenshot(box: Box):
    img = pyautogui.screenshot(region=(box.left, box.top, box.width, box.height))
    # img = ImageOps.grayscale(img)
    return img


WINDOW_NAME = "BlueStacks App Player"


def GetAppWindow():
    windowName = "BlueStacks App Player"
    try:
        hwnd = win32gui.FindWindow(None, windowName)
        if hwnd == 0:
            quit(f'Could not find window with title "{windowName}"')
    except Exception as e:
        quit(f'An error occurred while trying to find the window with title "{windowName}": {e}')

    # Bring the window to the foreground
    try:
        win32gui.SetForegroundWindow(hwnd)
        # Ensure the window is not minimized
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        time.sleep(1)
    except Exception as e:
        quit(f'An error occurred while trying to bring the window to the foreground: {e}')

    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    width = right - left
    height = bottom - top
    return Box(left, top, width, height)


# @CheckArguments
def GetOwnUnitsWindow(appWindow: Box):
    # UNITS BOX
    return Box(
        left=appWindow.left + 72,
        top=appWindow.top + 479,
        width=62 * appWindow.width / 100,
        height=int(appWindow.height / 4 - 25)
    )
