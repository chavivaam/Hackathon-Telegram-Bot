import requests
from utils.config import TELEGRAM_INIT_WEBHOOK_URL

requests.get(TELEGRAM_INIT_WEBHOOK_URL)
