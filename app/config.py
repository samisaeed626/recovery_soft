import os
from dotenv import load_dotenv
from pydantic import BaseSettings


load_dotenv()
class Settings(BaseSettings):
    """
    This class contains all the configuration variables,
    which can be imported from here into other modules and apps
    """
    app_name: str = "Rental Property Calculator"
    db_url: str = os.environ['DB_URL']

settings = Settings()
