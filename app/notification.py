import request
import json
TELEGRAM_URL = "https://api.telegram.org/bot"


class Telegram(object):
    def __init__(self, auth, bot_id):
        self.auth = auth
        self.bot_id = bot_id

    def get_bot_info(self):
        """ Get telegram bot info """

        URL = "f{TELEGRAM_URL}/{self.auth}/getMe"
        response = requests.get(URL)
        return json.dumps(response)

    def send_message(self, message):
        """ Send telegram message"""

        URL = "f{TELEGRAM_URL}/{self.auth}/sendMessage"
        params = {
            "chat_id": self.bot_id,
            "text": message
        }
        response = requests.post(URL, data=json.dumps(data))
        return response
