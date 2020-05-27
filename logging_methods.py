import logging

# DEBUG: Detailed information, typically of interest only when diagnosing problems.
# INFO: Confirmation that things are working as expected.
# WARNING: An indication that something unexpected happened, or indicative of some problem in
#         the near future (e.g. ‘disk space low’). The software is still working as expected.
# ERROR: Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

# for all available format options check LogRecord attributes at:
# https://docs.python.org/3/library/logging.html
logger = logging.getLogger(__name__)  # if imported from another module or script will get the name of that module or script
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s%(lineno)d')

file_handler = logging.FileHandler('test.log')
file_handler.setLevel(logging.ERROR) # to only capture info msg
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)
# to configure the root logger
# logging.basicConfig(filename='test.log', level=logging.DEBUG,
#                             format='%(asctime)s:%(levelname)s:%(message)s%(lineno)d')


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception('Tried to divide by zero')
    else:
        return result


num_1 = 20
num_2 = 0

add_result = add(num_1, num_2)
logger.info('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logger.info('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logger.info('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logger.info('Div: {} / {} = {}'.format(num_1, num_2, div_result))

