import configparser
import os
import pathlib

from dotenv import load_dotenv

load_dotenv()
PACKAGE_FOLDER = pathlib.Path(__file__).parent
config = configparser.ConfigParser()
config.read(pathlib.Path(PACKAGE_FOLDER, 'config.ini'))
config_general = config['general']

DEBUG = os.environ.get('DEBUG')
config_general['DEBUG'] = DEBUG
DEBUG = config_general.getboolean('DEBUG', False)
REFERRALS_API_HOST = config_general.get('REFERRALS_API_HOST')
REFERRALS_API_PORT = config_general.getint('REFERRALS_API_PORT')

if not DEBUG:
    HOST = config_general.get('HOST', 'localhost')
    PORT = config_general.getint('PORT', 8183)
else:
    HOST = config_general.get('TEST_HOST', 'localhost')
    PORT = config_general.getint('TEST_PORT', 8283)
