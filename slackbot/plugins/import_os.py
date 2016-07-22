import os
from slackbot.bot import respond_to

@respond_to('I love you')
def love(message):
    message.reply('I love you too!')