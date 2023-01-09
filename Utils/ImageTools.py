import uuid

import cv2
import numpy
import numpy as np
from PIL import Image
from matplotlib import cm

from Classes.Box import Box


def SaveImageLocally(image):
    print(image.shape)
    file_name = str(uuid.uuid4()) + '.png'
    file_path = 'C:\\Users\\Meiu\\Desktop\\RushRoyaleBot_v3\\assets\\Dryad\\' + file_name
    # Save the image to the file path
    cv2.imwrite(file_path, image)


# @MeasurePerformance
# @CheckArguments
def DrawContour(image: numpy.ndarray, box: Box, labelToShow: str):
    # Extract coordinates and dimensions of the bounding box
    left = int(box.left)
    top = int(box.top)
    width = int(box.width)
    height = int(box.height)

    labelToShow = labelToShow.upper()
    # Set the color of the bounding box
    rectangle_color = (36, 255, 12)

    # Draw the bounding box on the image
    image_with_box = cv2.rectangle(image, (left, top), (width, height), rectangle_color, 1)

    # Set the color of the text
    text_color = (255, 0, 12)

    # Set the color of the text background
    text_bg_color = (36, 255, 12)

    # Get the size of the text
    (text_width, text_height) = cv2.getTextSize(labelToShow, cv2.FONT_HERSHEY_TRIPLEX, 0.2, 2)[0]

    # Draw the text background on the image
    image_with_text_bg = cv2.rectangle(image_with_box, (left, top), (left + text_width + 2, top - text_height + 10),
                                       text_bg_color, cv2.FILLED)

    # Draw the label on the image
    image_with_label = cv2.putText(image_with_text_bg, labelToShow, (left + 5, top + 5),
                                   cv2.FONT_HERSHEY_DUPLEX, 0.2, text_color, 1)

    # Convert the image back to BGR format
    return image_with_label


# @CheckArguments
def CropImage(image: numpy.ndarray, box: Box):
    return image[int(box.top):int(box.height), int(box.left):int(box.width)]


def ConvertNumpyArrayToPillowImage(numpy_array):
    return Image.fromarray(np.uint8(cm.gist_earth(numpy_array) * 255))


def ConvertPilImageToNumpyArrayFromPath(path):
    return np.asarray(Image.open(path))


def ConvertImageToNumpyArray(img):
    return cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
