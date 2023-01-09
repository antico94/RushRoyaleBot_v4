import os
import time

import numpy as np
from PIL import Image
from tqdm import tqdm


def GetAllSubdirectoriesFromFolder(path):
    # Get a list of all subdirectories in the given path
    subdirectories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    # Sort the subdirectories in alphabetical order
    subdirectories.sort()
    return subdirectories


def ConvertImagesToArrays(baseDir):
    total_files = 0
    for subdir in os.listdir(baseDir):
        subdirPath = os.path.join(baseDir, subdir)
        if os.path.isdir(subdirPath):
            total_files += len([f for f in os.listdir(subdirPath) if f.endswith('.png')])

    with tqdm(total=total_files, unit='file') as pbar:
        start_time = time.time()
        for subdir in os.listdir(baseDir):
            subdirPath = os.path.join(baseDir, subdir)
            if os.path.isdir(subdirPath):
                newSubdirPath = os.path.join(baseDir, 'new_' + subdir)
                os.makedirs(newSubdirPath, exist_ok=True)
                for imageFile in os.listdir(subdirPath):
                    if imageFile.endswith('.png'):
                        imagePath = os.path.join(subdirPath, imageFile)
                        image = Image.open(imagePath)
                        # Convert the image to a numpy array
                        imageArray = np.array(image)
                        # Save the image array to a new file
                        newImagePath = os.path.join(newSubdirPath, imageFile)
                        np.save(newImagePath, imageArray)
                        pbar.update()

                        # Calculate and display the estimated time left
                        elapsed_time = time.time() - start_time
                        estimated_time = elapsed_time / pbar.n * pbar.total
                        pbar.set_description(f'{estimated_time:.2f} seconds left')


def MassRename(baseDir):
    for subdir in os.listdir(baseDir):
        if subdir.startswith('new_'):
            old_path = os.path.join(baseDir, subdir)
            new_path = os.path.join(baseDir, subdir[4:])
            os.rename(old_path, new_path)
