import os
from webex_bot.webex_bot import WebexBot
webex_token = os.environ["WEBEX_TOKEN"]
bot = WebexBot(webex_token)
