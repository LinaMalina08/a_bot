import aiohttp
import os
from dotenv import load_dotenv


load_dotenv()

WEATHER_API_KEY = os.environ['WEATHER_API_KEY']


async def get_weather(city_name: str):
    async with aiohttp.ClientSession() as session:
        params = {
            'q': city_name,
            'lang': 'ru',
            'units': 'metric',
            'appid': WEATHER_API_KEY
        }
        async with session.get(f'http://api.openweathermap.org/data/2.5/weather', params=params) as response:
            response.json_parsed = await response.json()
            return response
