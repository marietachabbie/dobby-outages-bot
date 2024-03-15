''' This module loads all environment variables '''

import os
from dotenv import load_dotenv

load_dotenv()

# constant variables
BOT_TOKEN = os.environ.get('TG_BOT_TOKEN')
