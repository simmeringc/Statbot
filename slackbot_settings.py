import os
import plotly.plotly as py
API_TOKEN = os.environ.get('SLACKBOT_API_TOKEN')
ERROR_TO = "general"
DEFAULT_REPLY = "Type '@statbot help' for a list of Statbot commands."
py.sign_in('simmeringc', os.environ.get('PLOTLY_API_KEY'))
