import os
from webex_bot.webex_bot import WebexBot

#retrive the api token that we export
# to export the token use export WEBEX_TOKEN= "Put the token here"

webex_token = os.environ["WEBEX_TOKEN"]
bot = WebexBot(webex_token)

bot.run()
