# -*- coding: utf-8 -*-
import telebot
from config import *
from telebot import types
from requests import get

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/help")
    keyboard.row("Привет")
    keyboard.row("Спит")
    keyboard.row("Вампир")
    keyboard.row("Летит")
    keyboard.row("Ест")
    keyboard.row("Наелся")
    bot.send_message(message.chat.id, 'Поприветствуй котиков :з', reply_markup=keyboard)



@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'hi')

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, 'Привет! А я тут котиков показываю. Нажми на кнопочку "/help", если тебе нужна помощь, либо выбери, какого котика ты хочешь посмотреть.')
    elif message.text.lower() == "спит":
        bot.send_message(message.chat.id, "Только не разбуди его!")
        bot.send_photo(message.chat.id, get("https://zagony.ru/uploads/posts/2014-12/1420023271_2.jpg").content)
    elif message.text.lower() == "вампир":
        bot.send_message(message.chat.id, "Прячься")
        bot.send_photo(message.chat.id, get("https://medialeaks.ru/wp-content/uploads/2017/10/1-8-500x500.jpg").content)
    elif message.text.lower() == "летит":
        bot.send_message(message.chat.id, "Прикольно, правда?")
        bot.send_photo(message.chat.id, get("https://sun9-78.userapi.com/impg/88P8ehYFooObIqR48Ee5W_cJwIKiIMcDhhm4BA/6pIy90ODKz8.jpg?size=610x610&quality=96&sign=73065fd55961477677196d14cfe70349&type=album").content)
    elif message.text.lower() == "ест":
        bot.send_message(message.chat.id, "Ты тоже иди покушай")
        bot.send_photo(message.chat.id, get("https://pbs.twimg.com/media/Eqv_nUdXMAApd2i.jpg").content)
    elif message.text.lower() == "наелся":
        bot.send_message(message.chat.id, "На самом деле он бы еще поел...")
        bot.send_photo(message.chat.id, get("https://funart.pro/uploads/posts/2021-07/1625805370_8-funart-pro-p-samaya-tolstaya-koshka-zhivotnie-krasivo-f-8.jpg").content)
    else :
        bot.send_message(message.chat.id, "Если тебе требуется помощь, нто напиши /help.." )


bot.polling()