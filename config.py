from dotenv import load_dotenv
import os
from pathlib import Path

from pydantic import BaseModel


load_dotenv(Path('.') / '.env')  # .env file path


class Config(BaseModel):
    debug_enabled: bool = os.getenv('DEBUG')
    host: str = os.getenv('HOST')
    port: int = int(os.getenv('PORT'))
    openweathermap_api_key: str = os.getenv('OPENWEATHERMAP_API_KEY')
