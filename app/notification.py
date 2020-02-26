import requests
import logging
import json
TELEGRAM_URL = "https://api.telegram.org"


class Telegram(object):
    def __init__(self, auth, bot_id):
        self.auth = auth
        self.bot_id = bot_id
        logging.debug(f"auth: {auth}")
        logging.debug(f"bot_id: {bot_id}")

    def get_bot_info(self):
        """ Get telegram bot info """

        URL = f"{TELEGRAM_URL}/bot{self.auth}/getMe"
        logging.debug(f"Request: {URL}")
        try:
            response = requests.get(URL).json()
            return json.dumps(response)
        except requests.exceptions.RequestException as e:
            logging.info(f"Failed to get info: {e}")
            return None

    def send_message(self, message):
        """ Send telegram message"""

        URL = f"{TELEGRAM_URL}/bot{self.auth}/sendMessage"
        params = {
            "chat_id": self.bot_id,
            "text": message
        }

        logging.debug(f"Request: {URL}")
        logging.debug(f"Params: {params}")
        try:
            response = requests.post(URL, params=params)
            return True
        except requests.exceptions.RequestException as e:
            logging.info(f"Failed to get info: {e}")
            return False
