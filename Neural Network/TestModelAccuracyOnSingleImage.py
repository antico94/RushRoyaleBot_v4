import os
import random

import numpy as np
import tensorflow.keras.utils as image
from tensorflow.keras.models import load_model

from Utils.OSTools import GetAllSubdirectoriesFromFolder

test_dir = 'C:/Users/Meiu/Desktop/unit'
class_label = GetAllSubdirectoriesFromFolder(test_dir)


# Define the classify_image function outside of the loop
def classify_image(image_path):
    # Load the model
    model = load_model('units_model.h5')
    img_width, img_height = 57, 57

    # Load and preprocess the image
    img = image.load_img(image_path, target_size=(img_width, img_height))
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.

    # Classify the image
    classes = model.predict(img_tensor, batch_size=1, verbose=0)
    class_index = np.argmax(classes[0])

    # Get the class label from the test data generator

    return class_label[class_index]


def get_random_image_path(base_dir):
    # Get a list of all subdirectories in the base directory
    subdirs = os.listdir(base_dir)

    # Pick a random subdirectory
    subdir = random.choice(subdirs)

    # Get a list of all files in the subdirectory
    files = os.listdir(os.path.join(base_dir, subdir))

    # Pick a random file
    file = random.choice(files)

    # Return the full path to the file
    return os.path.join(base_dir, subdir, file)


# Call classify_image in a loop

for i in range(100):
    pick = get_random_image_path('C:/Users/Meiu/Desktop/unit')
    print('True' if pick.split("unit")[1].split('\\')[1] == str(classify_image(pick)) else 'False')


def ClassifyPillowImage(image):
    # Load the model
    model = load_model('units_model.h5')
    img_tensor = image.img_to_array(image)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.

    # Classify the image
    classes = model.predict(img_tensor, batch_size=1, verbose=0)
    class_index = np.argmax(classes[0])

    # Get the class label from the test data generator

    return class_label[class_index]
