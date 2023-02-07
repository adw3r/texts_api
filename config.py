import os
import pathlib

from dotenv import load_dotenv

load_dotenv()
PACKAGE_FOLDER = pathlib.Path(__file__).parent

HOST = os.environ.get('HOST', '0.0.0.0')
PORT = os.environ.get('PORT', int('8183'))
REFERALS_API_HOST = os.environ.get('REFERALS_API_HOST')
REFERALS_API_PORT = os.environ.get('REFERALS_API_PORT')
