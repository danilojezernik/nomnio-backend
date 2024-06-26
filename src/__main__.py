from fastapi import FastAPI
import requests
import uvicorn

from src import env
from fastapi.middleware.cors import CORSMiddleware

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
@app.get('/weather')
def get_city_temp():
    # Constructing the API request URL with coordinates and unit of measurement.
    response = requests.get(
        f'http://api.openweathermap.org/data/2.5/forecast?lat={env.LAT}&lon={env.LON}&units={env.UNIT}&appid={env.API_KEY}')

    # Parsing the API response and returning it along with the HTTP status code.
    body = response.json()
    return body, response.status_code


if __name__ == '__main__':
    # Start the FastAPI application on localhost with the port number from environment settings.
    uvicorn.run(app, host="127.0.0.1", port=env.PORT)
