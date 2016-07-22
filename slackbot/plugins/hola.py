from slackbot.bot import respond_to

@respond_to('hola')
def hola(message):
    message.reply('yolloha')
