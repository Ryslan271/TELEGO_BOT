import random

import telebot
from models.start import bot
from telebot import types
from models.support import Vact


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '/start':
            Vact(message)

        elif message.text == 'Интересные факты':
            Vact(message)

        elif message.text == 'Купить сайт':
            Vact(message)

        elif message.text == 'Связаться':
            Vact(message)

        elif message.text == '/Назад':
            Vact(message)

        elif message.text == 'Пароль':
            Vact(message)

        elif message.text == '6 цифр':
            Vact(message)

        elif message.text == '8 цифр':
            Vact(message)


        else:
            msg = message.text
            bot.send_message(message.chat.id, 'Я не знаю что ответить вам на \"' + str(msg) + "\"")
