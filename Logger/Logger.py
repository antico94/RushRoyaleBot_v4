import logging


def CreateLogger(name):
    localLogger = logging.getLogger(name)
    localLogger.setLevel(logging.INFO)

    # Create a file handler to log messages to a file
    file_handler = logging.FileHandler("logs.txt")
    file_handler.setLevel(logging.INFO)

    # Create a stream handler to log messages to the console
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    # Create a formatter to specify the format of the log messages
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    # Add the handlers to the logger
    localLogger.addHandler(file_handler)
    localLogger.addHandler(stream_handler)

    return localLogger


logger = CreateLogger("my_logger")
