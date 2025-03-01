import os
from dotenv import load_dotenv


load_dotenv()


TOKEN = os.getenv("TOKEN")
DB_CONNECTION_STRING = os.getenv("DB_CONNECTION_STRING")


def get_setting(name: str):
    return os.getenv(name)
