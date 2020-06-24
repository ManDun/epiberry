"""
Module that contains methods to insert data into influxdb

To test this file, you can tun python3 influx.py

Uses logzero
"""

from influxdb import InfluxDBClient
from utils import const
from datetime import datetime
import socket
from logzero import logger

client = InfluxDBClient(host=const.DB_HOST, port=const.DB_PORT, username=const.DB_USER, password=const.DB_PASSWORD, database=const.DB_NAME_NETWORK)
logger.debug('InfluxDBClient created')

def log_status(status_code):
    """
    Input:
        int: Status code to insert value
    Returns:
        Boolean: Whether the connestion is on
    """
    try:
        logger.debug(f'Started log_status with code: {status_code}')

        client.create_database(const.DB_NAME_NETWORK)
        logger.debug('Database created')

        json_body = [
            {
                "measurement": const.DB_NET_STATUS,
                "tags": {
                    "host": socket.gethostname(),
                },
                "time": datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'),
                "fields": {
                    "value": status_code
                }
            }
        ]

        client.write_points(json_body)
        logger.debug('Data logged into influxdb')
        return True  
    except Exception as error:
        logger.error(f'Influxdb error inserting measurement: {error}')
        return False
    finally:
        logger.debug('Data insertion complete')


def log_speed(download_speed, upload_speed):
    """
    Input:
        int: Download speed

        int: Upload Speed
    Returns:
        Boolean: Whether the connestion is on
    """
    try:
        logger.debug(f'Started log_speed with code: {download_speed}, {upload_speed}')

        client.create_database(const.DB_NAME_NETWORK)
        logger.debug('Database created')

        json_body = [
            {
                "measurement": const.DB_NET_SPEED,
                "tags": {
                    "host": socket.gethostname(),
                },
                "time": datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'),
                "fields": {
                    "download": download_speed,
                    "upload": upload_speed
                }
            }
        ]

        client.write_points(json_body)
        logger.debug('Data logged into influxdb')
        return True  
    except Exception as error:
        logger.error(f'Influxdb error inserting measurement: {error}')
        return False
    finally:
        logger.debug('Data insertion complete')
    