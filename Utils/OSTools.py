import glob
import os
import time

import numpy as np
from PIL import Image
from tqdm import tqdm


def DeleteFilesByExtension(directory, extension):
    # Find all the files with the specified extension in the directory
    files = glob.glob(os.path.join(directory, f'*.{extension}'))

    # Delete the files
    for file in files:
        os.remove(file)


def GetSubdirectories(directory):
    subdirectories = []
    # Get a list of all the entries in the directory
    entries = os.listdir(directory)
    # Iterate over the entries
    for entry in entries:
        # Get the full path of the entry
        entry_path = os.path.join(directory, entry)
        # Check if the entry is a directory
        if os.path.isdir(entry_path):
            # If it is a directory, add it to the list of subdirectories
            subdirectories.append(entry_path)
    return subdirectories


def DeleteAllFiletypeFromRootFolder(directory, extension):
    # Get the list of subdirectories
    subdirectories = GetSubdirectories(directory)
    # Delete the files with the specified extension from each subdirectory
    for subdirectory in subdirectories:
        DeleteFilesByExtension(subdirectory, extension)


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
