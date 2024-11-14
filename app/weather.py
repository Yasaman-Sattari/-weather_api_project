# app/weather.py

import requests
from fastapi import HTTPException
from pydantic import BaseModel

WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"
API_KEY = "3b01dbe777c8e8b2332f9ef889739e21"  # Get your own API key from OpenWeatherMap

class WeatherResponse(BaseModel):
    temperature: float
    description: str
    city: str

def fetch_weather(city: str) -> WeatherResponse:
    """
    Fetches the weather data from OpenWeather API and returns a WeatherResponse model.
    """
    try:
        response = requests.get(WEATHER_API_URL, params={
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        })
        data = response.json()

        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="City not found")

        return WeatherResponse(
            temperature=data['main']['temp'],
            description=data['weather'][0]['description'],
            city=city
        )
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
