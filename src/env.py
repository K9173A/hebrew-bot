import os

from dotenv import load_dotenv


load_dotenv()

token = os.getenv('BOT_TOKEN')
dev_mode = os.getenv('DEV_MODE', False)
