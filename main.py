from fastapi import FastAPI,HTTPException
import httpx
from datetime import datetime
import os



from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="☁🌞")

test_id = os.getenv("a809458ee94fc0c2678e48bfb541c3b9")
BASE_URL = f"https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid={test_id}"


@app.get("/weather/{city}")
async def get_weather(city:str):

    current_date = datetime.now().strftime("%Y-%m-%d")

    

    params = {
        "q": "city",
        "k":"country",
        "appid": test_id,
        "units": "metric"

    }
    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params= params)

        if response.status_code !=200:
            raise HTTPException(status_code=response.status_code, detail="Error occurred while fetching weather data")
        data = response.json()

        weather_data = {
        "city": data["city"],
        "country": data["sys"]["country"],
        "date": current_date,
        "sunrise": datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%Y-%m-%d %H:%M:%S"),
        "sunset": datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%Y-%m-%d %H:%M:%S"),
        "timezone": data["timezone"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"]
        
        }

        return weather_data






