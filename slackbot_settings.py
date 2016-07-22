import os
API_TOKEN = os.environ.get('SLACKBOT_API_TOKEN')
ERROT_TO = "general"
PLUGINS = [
    'slackbot.plugins',
]
DEFAULT_REPLY = "Sorry but I didn't understand you"
