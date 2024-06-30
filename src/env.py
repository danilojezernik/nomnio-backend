import os

from dotenv import load_dotenv

load_dotenv()
PORT = int(os.getenv('PORT'))
API_KEY = os.getenv('API_KEY')
LAT = int(os.getenv('LAT'))
LON = int(os.getenv('LON'))
UNIT = os.getenv('UNIT')
