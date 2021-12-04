# -*- coding: utf-8 -*-
import telebot
from config import *
from telebot import types
from requests import get

bot = telebot.TeleBot(token)

cats= {'спит': 'Только не разбуди его!',
       'вампир': "Прячься",
       'летит':"Прикольно, правда?",
       'ест':"Ты тоже иди покушай",
       'наелся':"На самом деле он бы еще поел..."}

photo= {'спит': "https://zagony.ru/uploads/posts/2014-12/1420023271_2.jpg" ,
       'вампир': "https://medialeaks.ru/wp-content/uploads/2017/10/1-8-500x500.jpg",
       'летит':"https://sun9-78.userapi.com/impg/88P8ehYFooObIqR48Ee5W_cJwIKiIMcDhhm4BA/6pIy90ODKz8.jpg?size=610x610&quality=96&sign=73065fd55961477677196d14cfe70349&type=album",
       'ест':"https://pbs.twimg.com/media/Eqv_nUdXMAApd2i.jpg",
       'наелся':"https://funart.pro/uploads/posts/2021-07/1625805370_8-funart-pro-p-samaya-tolstaya-koshka-zhivotnie-krasivo-f-8.jpg"}


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Привет")
    keyboard.row("Спит")
    keyboard.row("Вампир")
    keyboard.row("Летит")
    keyboard.row("Ест")
    keyboard.row("Наелся")
    bot.send_message(message.chat.id, 'Поприветствуй котиков :з', reply_markup=keyboard)



@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Выбери нужного тебе котика в кнопках, либо отправь:\n'\
                                      '"Спит" - появится спящий котик;\n'\
                                      '"Вампир" - появится котик Дракула;\n'\
                                      '"Летит" - появится летающий котик;\n'\
                                      '"Ест" - появится кушающий котик;\n'\
                                      '"Наелся" - появится котик, который уже покушал;\n\n'\
                                      'Удачи!')


@bot.message_handler(commands=['day'])
def start_message(message):
    bot.send_message(message.chat.id, 'О, ты хочешь узнать какой ты сегодня котик? Ну, лови :з')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, 'Привет! А я тут котиков показываю. Нажми на кнопочку "/help", если тебе нужна помощь, либо выбери, какого котика ты хочешь посмотреть.')
    elif message.text.lower() in cats:
        bot.send_message(message.chat.id, cats.get( message.text.lower() ) )
        bot.send_photo(message.chat.id, get( photo.get( message.text.lower()) ).content)
    else :
        bot.send_message(message.chat.id, "Если тебе требуется помощь, нто напиши /help.." )


bot.polling()