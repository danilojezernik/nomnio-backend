import requests
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from src import env

app = FastAPI()

# CORS configuration to allow requests from any origin, supporting all methods and headers.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# API route to fetch weather forecast data at 3-hour intervals over the next 5 days for Maribor.
@app.get('/weather-forecast')
def get_city_temp():
    """
    Fetches weather forecast data for Maribor using OpenWeatherMap API.
    """

    # Constructing the API request URL with coordinates and unit of measurement.
    response = requests.get(
        f'https://api.openweathermap.org/data/2.5/forecast?lat={env.LAT}&lon={env.LON}&units={env.UNIT}&appid={env.API_KEY}')

    # Checking if request was successful (status code 200)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch weather data")

    # Parsing the API response and returning specific data fields.
    body = response.json()

    return body, response.status_code


# API route to fetch current weather data for Maribor.
@app.get('/weather-current')
def get_forecast():
    """
    Fetches current weather data for Maribor using OpenWeatherMap API.
    """

    # Constructing the API request URL with coordinates and unit of measurement for current weather data.
    response = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather?lat={env.LAT}&lon={env.LON}&units={env.UNIT}&appid={env.API_KEY}')

    # Checking if request was successful (status code 200)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch current weather data")

    # Parsing the API response and returning it along with the HTTP status code.
    body = response.json()

    return body, response.status_code


if __name__ == '__main__':
    # Start the FastAPI application on localhost with the port number from environment settings.
    uvicorn.run(app, host="127.0.0.1", port=env.PORT)
