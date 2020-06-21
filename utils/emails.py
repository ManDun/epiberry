from getpass import getpass
import os
from utils import const
from logzero import logger


def setup_email():
    try:
        logger.debug('Starting email setup')
        email = input('Enter your email id: ')
        password = getpass()

        os.environ[const.EMAIL_USER] = email
        os.environ[const.EMAIL_PASSWORD] = password

    except Exception as e:
        logger.error(f'Error setting environment for email: {e}')
    finally:
        logger.debug('Email setup complete')


def send_html_email():
    try:
        pass

    except Exception as e:
        pass
        
    finally:
        pass
    
