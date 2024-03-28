''' This module loads all environment variables '''

import os
from dotenv import load_dotenv

load_dotenv()

# constant variables
BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")
DATABASE = os.environ.get("DATABASE")
DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_PORT = os.environ.get("DB_PORT")
