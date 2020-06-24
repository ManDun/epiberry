"""
Module that contains methods to perform network operations

To test this file, you can tun python3 network.py

Uses logzero
"""

import urllib.request
from logzero import logger
from utils import const
import ssl
from utils import influx
import speedtest


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

        logger.info(f'Response Code: {response_code}')
        influx.log_status(response_code)

        if response_code == const.SUCCESS_CODE:
            return True
        else:
            return False

    except urllib.request.URLError as error:
        logger.error(f'URL Error: {error}')
        return False

    finally:
        logger.debug('Test complete')


def speed_test():
    """
    
    """
    try:
        logger.debug(f'Speed test start')

        st = speedtest.Speedtest()
        download_speed = round(st.download()/1000000, 2)
        upload_speed = round (st.upload()/1000000, 2)

        logger.info(f'Download: {download_speed}, Upload: {upload_speed}')

        influx.log_speed(download_speed, upload_speed)

    except Exception as error:
        logger.error(f'URL Error: {error}')
        return False

    finally:
        logger.debug('Test complete')


if __name__ == "__main__":
    print(check_internet_on())
