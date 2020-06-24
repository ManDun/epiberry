#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Manas Mallilck"
__version__ = "0.1.0"
__license__ = "MIT"

import sys
import os
from logzero import logger, logfile, loglevel
from utils import network, const, emails
import logging

log_file = os.path.join(const.LOG_FOLDER, const.LOG_FILE + '.log')

logfile(log_file, maxBytes=1000000, backupCount=3)
loglevel(level=logging.INFO)

arguments = sys.argv

if len(arguments) > 1:
    method_name = arguments[1]
else:
    logger.error('No arguments supplied')
    exit(0)


def main():
    """ Main entry point of the app """
    logger.debug('Started from main')

    if method_name in const.SETUP_EMAIL:
        emails.setup_email()
    elif method_name in const.CHECK_NETWORK:
        network.check_internet_on()
    elif method_name in const.SPEED_TEST:
        network.speed_test()
    else:
        logger.error(f'Invalid argument: {method_name}')
    logger.debug('End from main')


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
