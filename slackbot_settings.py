import os
API_TOKEN = os.environ.get('SLACKBOT_API_TOKEN')
ERROT_TO = "general"
DEFAULT_REPLY = "Sorry but I didn't understand you"
PLUGINS = [
   'slackbot.plugins',
   'mybot.plugins'
]
