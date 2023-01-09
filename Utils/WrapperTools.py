import inspect
import timeit

from Logger.Logger import logger


def CheckArguments(func):
    def wrapper(*args, **kwargs):
        # Get the argument names and default values of the function
        sig = inspect.signature(func)
        arg_names = list(sig.parameters.keys())
        defaults = {k: v.default for k, v in sig.parameters.items() if v.default is not inspect.Parameter.empty}
        frame = inspect.stack()[1]
        filename = frame.filename
        line_number = frame.lineno
        function_name = frame.function

        # Check the number of arguments
        if len(args) > len(arg_names):
            quit(f"{func.__name__}() takes at most {len(arg_names)} arguments ({len(args)} given)")

        # Check the types of the arguments
        for i, (arg, expected_type) in enumerate(zip(args, sig.parameters.values())):
            if not isinstance(arg, expected_type.annotation):
                quit(f"In the {func.__name__}() function, filename: {filename[17:]}, line number: {line_number}"
                     f"\n the argument \'{arg_names[i]}\' must be {expected_type.annotation} but received {type(arg).__name__}.")

        # Check the types of the keyword arguments
        for name, value in kwargs.items():
            if name not in arg_names:
                quit(f"{func.__name__}() got an unexpected keyword argument '{name}'")
            expected_type = sig.parameters[name].annotation
            if not isinstance(value, expected_type):
                quit(f"{func.__name__}() argument {name} must be {expected_type} (got {type(value).__name__})")

        # Call the function with the checked arguments
        return func(*args, **kwargs)

    return wrapper


def LogFunctionCall(func):
    def wrapper(*args, **kwargs):
        # Get the calling frame
        frame = inspect.stack()[1]
        # Get the name of the calling function
        caller_name = frame[3]
        # Log the function call
        logger.info(f"{caller_name} called function {func.__name__} with args {args} and kwargs {kwargs}")
        # Call the function
        result = func(*args, **kwargs)
        return result

    return wrapper


def MeasurePerformance(func):
    def wrapper(*args, **kwargs):
        start = timeit.default_timer()
        result = func(*args, **kwargs)
        end = timeit.default_timer()
        print(f'{func.__name__} took {end - start:.6f} seconds to complete')
        return result

    return wrapper
