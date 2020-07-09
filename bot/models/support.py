import random

import telebot
from models.start import bot
from telebot import types


@bot.message_handler()
class Vact:
    def __init__(self, message):
        self.message = message

        if message.text == '/start':
            Vact.start_t(self, self.message)

        elif message.text == 'Интересные факты':
            Vact.vact1(self, self.message)

        elif message.text == '/Назад':
            Vact.osnova_1(self, self.message)

        elif message.text == 'Пароль':
            Vact.passw(self, self.message)

        elif message.text == '6 цифр':
            Vact.password_6(self, self.message)

        elif message.text == '8 цифр':
            Vact.password_8(self, self.message)

        elif message.text == 'Связаться':
            Vact.svaz(self, self.message)

        elif message.text == 'Купить сайт':
            Vact.buy_web(self, self.message)

        else:
            Vact.aga(self, self.message)


    def vact1(self, message):
        if message.text == 'Интересные факты':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            item4 = types.KeyboardButton("Ага")
            item5 = types.KeyboardButton("Ну такое кнч")
            item1 = types.KeyboardButton("/Назад")

            markup.add(item4, item5, item1)

            bot.send_message(message.chat.id,
                             "Мне было скучно и я решил создать это чудо\nСогласись прикольно?", reply_markup=markup)
            Vact.aga(self, self.message)

    def aga(self, message):
        if message.text == 'Ага':
            bot.send_message(message.chat.id,
                             "дай пять брооооооооооо")
            Vact.osnova_1(self, self.message)

        else:
            Vact.ny_tc(self, self.message)

    def ny_tc(self, message):
        if message.text == 'Ну такое кнч':
            bot.send_message(message.chat.id,
                             "эээээ ну прикольно же че ты")
            Vact.osnova_1(self, self.message)

        else:
            pass

    def osnova_1(self, message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        item1 = types.KeyboardButton("Интересные факты")
        item2 = types.KeyboardButton("Пароль")
        item3 = types.KeyboardButton("Купить сайт")

        markup.add(item1, item2, item3)

        bot.send_message(message.chat.id,
                         "Ну что же выбери , что дальше будем делать", reply_markup=markup)

    def passw(self, message):
        if message.text == 'Пароль':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            item6 = types.KeyboardButton("6 цифр")
            item7 = types.KeyboardButton("8 цифр")
            item1 = types.KeyboardButton("/Назад")

            markup.add(item6, item7, item1)

            bot.send_message(message.chat.id, 'Пароль на 6 или на 8?',
                             reply_markup=markup)
        else:
            pass

    def password_6(self, message):
        chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890#VsevlodHtml#'
        number = int(1)
        length = int(6)
        for n in range(number):
            password = ''
            for i in range(length):
                password += random.choice(chars)
        bot.send_message(message.chat.id,
                         password)
        Vact.osnova_1(self, self.message)

    def password_8(self, message):
        chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890#VsevlodHtml#'
        number = int(1)
        length = int(8)
        for n in range(number):
            password = ''
            for i in range(length):
                password += random.choice(chars)
        bot.send_message(message.chat.id,
                         password)
        Vact.osnova_1(self, self.message)

    def svaz(self, message):
        bot.send_message(message.chat.id,
                         "У меня есть\n"
                         '<a href="https://wa.me/+79272413062">Ватсапп</a>\n'
                         '\n'
                         '<a href="https://t.me/Dog_Python">Телега</a>\n',
                         parse_mode='html')
        Vact.osnova_1(self, self.message)

    def buy_web(self, message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        item4 = types.KeyboardButton("Связаться")
        item1 = types.KeyboardButton("/Назад")

        markup.add(item4, item1)

        bot.send_message(message.chat.id,
                         '<b>Опыт работы - мои проекты:</b>\n<a href="https://rupit.herokuapp.com/">Сайт по '
                         'обущению на языке питон</a>\n'
                         'Закончил обущение в <a href="https://yandexlyceum.ru/">Яндекс лицее</a>',
                         parse_mode='html', reply_markup=markup)

    def start_t(self, message):
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

