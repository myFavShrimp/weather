from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import httpx

from config import Config


app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), 'static')

templates = Jinja2Templates('templates')

api_key = Config().openweathermap_api_key


@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@app.get('/favicon.ico')
async def index(request: Request):
    print('lol')
    return 'lol'


@app.get('/{city}')
def city(request: Request, city: str):
    openweather_data = httpx.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}')
    if openweather_data.status_code != 200:
        return templates.TemplateResponse('index.html', {'request': request, 'title': openweather_data.status_code})

    city_data = openweather_data.json()

    return templates.TemplateResponse('index.html', {
                                                        'request': request,
                                                        'title': city,
                                                        'weather_data': city_data['weather'][0],
                                                        'temp_data': city_data['main'],
                                                        'wind_data': city_data['wind'],
                                                        'updated_on': city_data['dt'],
                                                     })
