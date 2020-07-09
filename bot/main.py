from models.start import bot
from models.users import lalala
from models.support import help_sup


@bot.message_handler(commands=['start'])
def welcome(message):
    lalala1(message)


@bot.message_handler(commands=['help'])
def help(message):
    help_sup(message)


@bot.message_handler(content_types=['text'])
def lalala1(message):
    lalala(message)


bot.polling(none_stop=True)
