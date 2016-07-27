from slackbot.bot import Bot
from slackbot import settings
from slackbot.bot import respond_to

def main():
    @respond_to('hola')
    def hola(message):
        message.reply('yolloha')
    bot = Bot()
    bot.run()

if __name__ == "__main__":
    main()
