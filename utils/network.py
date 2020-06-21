"""
Module that contains methods to perform network operations

To test this file, you can tun python3 network.py

Users logzero
"""

import urllib.request
from logzero import logger
from utils import const
import ssl


ssl._create_default_https_context = ssl._create_unverified_context


def check_internet_on():
    """
    Returns:
        Boolean: Whether the connestion is on
    """
    try:
        logger.debug(f'Open test url {const.TEST_URL}')
        response = urllib.request.urlopen(const.TEST_URL, timeout=1)
        response_code = response.getcode()

        logger.info(f'URL open with response: {response_code}')

        if response_code == const.SUCCESS_CODE:
            return True
        else:
            return False

    except urllib.request.URLError as error:
        logger.error(f'URL Error: {error}')
        return False

    finally:
        logger.debug('Test complete')


if __name__ == "__main__":
    print(check_internet_on())
