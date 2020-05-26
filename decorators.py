# some decorator functionality. Decorators add functionality to existing functions
# bu adding that functionality to the wrapper function.
# link to the video:
# https://www.youtube.com/watch?v=FsAPt_9Bf3U&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=37

from functools import wraps
log_path = 'logs/'

# this is a good boilerplate template for building all kinds of decorators:
def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator


# example how to add arguments to the decorator (basically adding nested layers)
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


# other decorator: s low_down function (f.i. when calling API's)
def slow_down(func):
    import time
    @wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down

@slow_down
def count_down(from_number):
    if from_number < 1:
        print("too low")
    else:
        print(from_number)
        count_down(from_number - 1)

count_down(5)


# Registering Plugins
# Decorators don’t have to wrap the function they’re decorating. They can also
# simply register that a function exists and return it unwrapped.
# This can be used, for instance, to create a light-weight plug-in architecture:
import random
PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)

randomly_greet("Alice")