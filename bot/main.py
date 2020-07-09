from models.start import bot
from models.users import lalala


@bot.message_handler(commands=['start'])
def welcome(message):
    lalala(message)


@bot.message_handler(commands=['help'])
def help(message):
    lalala(message)


bot.polling(none_stop=True)
