# -*- coding: utf-8 -*-
import telebot
from telebot import types
from requests import get


token = "2107957269:AAHMopQiead7oFZOIzrJwRXVtVfVyh4IRcs"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Привет!", "/help", "Спит", "Вампир", "Летит", "Ест", "Наелся")
    bot.send_message(message.chat.id, 'Привет!', reply_markup=keyboard)



@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'hi')

@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "Привет!":
        bot.send_message(message.chat.id, 'Привет! А я тут котиков показываю. Нажми на кнопочку "/help", если тебе нужна помощь, либо выбери, какого котика ты хочешь посмотреть.', reply_markup=keyboard)
    elif message.text.lower() == "Спит":
        bot.send_message(message.chat.id, "Только не разбуди его!", reply_markup=keyboard)
        bot.send_photo(message.chat.id, get("https://zagony.ru/uploads/posts/2014-12/1420023271_2.jpg").content)
    elif message.text.lower() == "Вампир":
        bot.send_message(message.chat.id, "Прячься", reply_markup=keyboard)
        bot.send_photo(message.chat.id, get("https://medialeaks.ru/wp-content/uploads/2017/10/1-8-500x500.jpg").content)
    elif message.text.lower() == "Летит":
        bot.send_message(message.chat.id, "Прикольно, правда?", reply_markup=keyboard)
        bot.send_photo(message.chat.id, get("https://zagony.ru/uploads/posts/2014-12/1420023271_2.jpg").content)
    elif message.text.lower() == "Ест":
        bot.send_message(message.chat.id, "Ты тоже иди покушай", reply_markup=keyboard)
        bot.send_photo(message.chat.id, get("https://pbs.twimg.com/media/Eqv_nUdXMAApd2i.jpg").content)
    elif message.text.lower() == "Наелся":
        bot.send_message(message.chat.id, "На самом деле он бы еще поел...", reply_markup=keyboard)
        bot.send_photo(message.chat.id, get("https://funart.pro/uploads/posts/2021-07/1625805370_8-funart-pro-p-samaya-tolstaya-koshka-zhivotnie-krasivo-f-8.jpg").content)


bot.polling()