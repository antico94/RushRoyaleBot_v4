import tkinter as tk
from tkinter import simpledialog

import cv2
from PIL import Image, ImageTk


from Utils.GameTools import CreateBoard, SetTilesBoxes
from Utils.PhotoTools import CropImage
from Utils.ScreenTools import GetAppWindow, GetOwnUnitsWindow, GetScreenshot
from Utils.Utils import ConvertImageToNumpyArray, IsPropertyPresent, SaveUnitToJson, GetColorsAverage
from Classes.Unit import Unit
from Classes.UnitCalibration import UnitCalibration


def StartCalibration(arrays, unitName):
    jsonFile = 'C:\\Users\\Meiu\\Desktop\\RushRoyaleBot_v3\\json\\units.json'
    # unitsColors = [dominant_colors(x, 3) for x in arrays]
    # print(unitsColors)
    # quit()
    # unitColorsAverage = GetColorsAverage(unitsColors)
    # unitsCalibration = [UnitCalibration().ImportValuesFromJson(x) for x in unitColorsAverage]
    # newUnit = Unit(name=unitName, colorList=[unitsCalibration[0], unitsCalibration[1], unitsCalibration[2]])
    #
    # if IsPropertyPresent(jsonFile, propertyValue=unitName, propertyName='name'):
    #     # IsCloseEnough(colors, unitName)
    #     print("Present")
    # else:
    #     SaveUnitToJson(jsonFile, newUnit)


def selectUnit(arrays):
    # Create the root window and a 3x5 grid of labels
    root = tk.Tk()
    grid = [[tk.Label(root) for _ in range(5)] for _ in range(3)]
    for i in range(3):
        for j in range(5):
            grid[i][j].grid(row=i, column=j)

    # Add a button to submit the selection
    def submit():
        # Get the indices of the selected arrays
        indices = [i * 5 + j for i in range(3) for j in range(5) if grid[i][j]['bg'] == 'green']
        # Get the selected arrays
        selection = [arrays[i] for i in indices]
        # Get the name of the unit from an input box
        name = simpledialog.askstring("Name", "Enter the name of the unit:")
        # Destroy the window
        root.destroy()
        # Return the selected arrays and the name of the unit
        return StartCalibration(selection, name)

    # Create image objects from the numpy arrays and display them in the labels
    for i in range(3):
        for j in range(5):
            image = Image.fromarray(cv2.cvtColor(arrays[i * 5 + j], cv2.COLOR_BGR2RGB))
            image = image.resize((100, 100), Image.Resampling.LANCZOS)
            image = ImageTk.PhotoImage(image)
            grid[i][j].config(image=image)
            grid[i][j].image = image
            grid[i][j].bind("<Button-1>", lambda event: toggleSelection(event.widget))

    tk.Button(root, text="Submit", command=submit).grid(row=4, column=2)
    root.mainloop()


def toggleSelection(widget):
    if widget['bg'] == 'green':
        widget['bg'] = 'white'
    else:
        widget['bg'] = 'green'


def Logic():
    appWindow = GetAppWindow()
    unitsWindow = GetOwnUnitsWindow(appWindow)
    board = CreateBoard()
    SetTilesBoxes(board=board, ownUnitsWindow=unitsWindow)
    data = []
    for tile in board.GetAllTiles():
        window = tile.window
        croppedImage = CropImage(ConvertImageToNumpyArray(GetScreenshot(unitsWindow)), window)
        data.append(croppedImage)
    selectUnit(data)


Logic()
