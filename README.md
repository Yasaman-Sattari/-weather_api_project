# Weather Forecast API with FastAPI

This is a simple weather forecast API built with **FastAPI**. The API allows users to get the current weather information for any city. The data is fetched from the **OpenWeatherMap** API, and the results are returned in a structured format. The project also includes a simple HTML interface to interact with the API.

## Features

- Get current weather data (temperature, description) for any city.
- Built with **FastAPI** for efficient API development.
- Beautiful, responsive user interface using HTML & CSS.
- Follows **Clean Code** principles and proper OOP structure.
- Structured commenting in English, following **Clean Code** guidelines.

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- Requests

You can install the necessary dependencies by running:

```bash
pip install -r requirements.txt


Where the requirements.txt file includes:

Copy code
fastapi
uvicorn
requests


Setup
1-Install the required dependencies using the command above.
2-Sign up at OpenWeatherMap to get your API key.
3-Replace the placeholder your_api_key_here in the main.py file with your actual API key.
4-Run the FastAPI server with:
uvicorn app.main:app --reload
This will start the server at http://127.0.0.1:8000.


How to Use
- Open your browser and visit http://127.0.0.1:8000.
- You will see a simple form asking for the name of the city.
- Enter the city name and click "Get Weather" to fetch the current weather data.
- The weather data (temperature and description) will be displayed below the form.


API Endpoints

/get_weather (POST)
- Description: Fetches the current weather for the specified city.
- Parameters:
    city (string): The name of the city.
-Response:
    temperature (float): Current temperature in Celsius.
    description (string): Weather description (e.g., clear sky, rainy).
    city (string): Name of the city.


Example request:
POST /get_weather
{
    "city": "London"
}


Example response:
{
    "temperature": 15.3,
    "description": "clear sky",
    "city": "London"
}


Acknowledgements
-The weather data is provided by OpenWeatherMap API.
-FastAPI for the fast and easy-to-use framework.
-Requests library for making HTTP requests.

