import os
from slackbot.bot import respond_to
API_TOKEN = os.environ.get('SLACKBOT_API_TOKEN')
ERROT_TO = "general"
PLUGINS = [
    'slackbot.plugins',
]
DEFAULT_REPLY = "Sorry but I didn't understand you!!"

@respond_to('hola')
def hola(message):
    message.reply('yolloha')
