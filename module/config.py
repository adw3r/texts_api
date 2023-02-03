import os
import pathlib

from dotenv import load_dotenv

load_dotenv()
PACKAGE_FOLDER = pathlib.Path(__file__).parent.parent

HOST = os.environ.get('HOST', '0.0.0.0')
PORT = os.environ.get('PORT', int('8183'))
