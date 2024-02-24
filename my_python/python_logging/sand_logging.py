#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def my_sand_logging(debug_level='WARNING'):
    """Boilerplate code to set up logging within a function

    Variables:
        debug_level (str): debug level to setup debug to

    References:
        Using a variable while calling logger.setLevel
        https://stackoverflow.com/questions/10332748/using-a-variable-while-calling-logger-setlevel
    """

    # imports, Python core modules
    import logging

    # Create a custom logger and set debug level
    logger = logging.getLogger(__name__)
    # need the following line to first baseline logging, do not know why though
    # https://docs.python.org/3/howto/logging-cookbook.html#logging-cookbook
    logger.setLevel(logging.DEBUG)

    # Create handler(s) and set the debug level
    c_handler = logging.StreamHandler()     # console handler
    c_handler.setLevel(debug_level)         # set debug level

    # Create formatter(s) and add to handlers
    # see available fields here:
    # https://docs.python.org/3/library/logging.html#logrecord-attributes
    c_format = logging.Formatter('%(asctime)s: %(module)s: %(funcName)s: %(lineno)d: %(name)s: %(levelname)s: %(message)s')
    c_handler.setFormatter(c_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)

    # here starts the normal file
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning')
    logger.error('This is an error')
    logger.critical('This is a critical message')

    # Python 3's f-Strings
    # https://realpython.com/python-f-strings/
    name = 'Lucy Lou'
    logger.debug(f'This is a debug log message from {name} using the f-string formating')


if __name__ == '__main__':
    level = 'DEBUG'
    # level = 'INFO'
    my_sand_logging(level)  # to pass a specific logging level
    # my_sand_logging()       # to use default logging level (which is WARNING)
