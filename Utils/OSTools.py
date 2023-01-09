import os


def GetAllSubdirectoriesFromFolder(path):
    # Get a list of all subdirectories in the given path
    subdirectories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    # Sort the subdirectories in alphabetical order
    subdirectories.sort()
    return subdirectories
