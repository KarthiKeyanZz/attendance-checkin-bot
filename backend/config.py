from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")
    LOCATION = os.getenv("LOCATION")
    NAME = os.getenv("NAME")


settings = Settings()