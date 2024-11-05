

from fastapi import FastAPI,HTTPException
import httpx
from datetime import datetime
import os



from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="☁🌞")

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


@app.get("/weather/{city}")
async def get_weather(city: str):

    current_date = datetime.now().strftime("%Y-%m-%d")

    

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"

    }
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params= params)

        if response.status_code !=200:
            raise HTTPException(status_code=response.status_code, detail="Error occurred while fetching weather data")
        data = response.json()

        weather_data = {
        "city": data["name"],
        