import uvicorn

from app import app
from config import Config


if __name__ == '__main__':
    if not Config().openweathermap_api_key:
        print('ERROR : No API key specified. Please add one to your \'.env\'.')
        exit()
    uvicorn.run(app, host=Config().host, port=Config().port, debug=Config().debug_enabled)
