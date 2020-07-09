import random

import telebot
from models.start import bot
from telebot import types
from models.support import help_sup, Vact


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '/start':
            sti = open('assets/hi.tgs', 'rb')
            bot.send_sticker(message.chat.id, sti)

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Интересные факты")
            item2 = types.KeyboardButton("Пароль")
            item3 = types.KeyboardButton("Купить сайт")

            markup.add(item1, item2, item3)

            bot.send_message(message.chat.id,
                             "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный для "
                             "разных прикольных фишек и кнч для рекламы :D".format(
                                 message.from_user, bot.get_me()),
                             parse_mode='html', reply_markup=markup)

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
