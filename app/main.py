# app/main.py

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import requests
from fastapi import Request

# Initialize FastAPI application
app = FastAPI()

# Set up Jinja2 templates
templates = Jinja2Templates(directory="app/templates")

# Define the Weather API endpoint
WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"
API_KEY = "3b01dbe777c8e8b2332f9ef889739e21"  # You must get your own API key from OpenWeatherMap

# Create a Pydantic model for the response
class WeatherResponse(BaseModel):
    temperature: float
    description: str
    city: str


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """
    Render the home page with input form for city name.
    """
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/get_weather", response_model=WeatherResponse)
async def get_weather(city: str):
    """
    Fetch weather data from the OpenWeather API.
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

        weather_data = WeatherResponse(
            temperature=data['main']['temp'],
            description=data['weather'][0]['description'],
            city=city
        )
        return weather_data
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))
