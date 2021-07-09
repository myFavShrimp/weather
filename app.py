from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import httpx

from config import Config
from utils import cache
from utils.helper import get_result_data


app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), 'static')

templates = Jinja2Templates('templates')

api_key = Config().openweathermap_api_key
cache_enabled = Config().cache_enabled


@app.get('/')
async def index(request: Request):

    return templates.TemplateResponse('index.html', {'request': request})


@app.get('/{city}')
def city(request: Request, city: str):
    if cache_enabled:
        if item := cache.get_cached_result(city):
            return templates.TemplateResponse('search.html', {'request': request} | get_result_data(item))

    openweather_data = httpx.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}')

    if openweather_data.status_code != 200:
        return templates.TemplateResponse('index.html',
                                          {'request': request} | {'title': openweather_data.status_code})

    city_data = openweather_data.json()
    cache.add_cached_result(city, city_data)

    return templates.TemplateResponse('search.html', {'request': request} | get_result_data(city_data))
