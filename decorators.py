# some decorator functionality. Decorators add functionality to existing functions
# bu adding that functionality to the wrapper function.
import time
from functools import wraps
log_path = 'logs/'


def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function


# example how to add arguments to the decorator:
def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
        # to accept any arbitrary number of positional pr keyword arguments
            print(prefix, f"wrapper executed {original_function.__name__}")
            return original_function(*args, **kwargs)
        return wrapper_function
    return decorator_function


class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f"call method executed {self.original_function.__name__}")
        return self.original_function(*args, **kwargs)


@decorator_class  # same as `display = decorator_function(display)`
def display():
    print("Display function ran")


#######
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=log_path + f'{orig_func.__name__}.log',
                        level=logging.INFO,
                        format="%(asctime)s — %(name)s — %(levelname)s —" "%(funcName)s:%(lineno)d — %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S")
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            f'Ran with args: {args}, and kwargs: {kwargs}')
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper


# @my_logger
# @my_timer
@prefix_decorator('LOG:')
def display_info(name, age):
    print(f"display_info ran w arguments: {name}, {age}")


display_info("diederik", 41)