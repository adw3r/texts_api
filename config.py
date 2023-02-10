import configparser
import os
import pathlib

from dotenv import load_dotenv

load_dotenv()
PACKAGE_FOLDER = pathlib.Path(__file__).parent
config = configparser.ConfigParser()

HOST = config['general'].get('HOST', 'localhost')
PORT = config['general'].getint('PORT', 8183)
REFERRALS_API_HOST = os.environ.get('REFERRALS_API_HOST')
REFERRALS_API_PORT = os.environ.get('REFERRALS_API_PORT')
