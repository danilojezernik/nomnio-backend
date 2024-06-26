import os

from dotenv import load_dotenv

load_dotenv()
PORT = int(os.getenv('PORT'))
API_KEY = os.getenv('API_KEY')
LAT = float(os.getenv('LAT'))
LON = float(os.getenv('LON'))
UNIT = os.getenv('UNIT')
