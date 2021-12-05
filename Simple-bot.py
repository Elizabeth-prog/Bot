# -*- coding: utf-8 -*-
import telebot
import random
from config import *
from telebot import types
from requests import get

bot = telebot.TeleBot(token)

cats= {'спит': 'Только не разбуди его!',
       'феникс': 'Знакомься, это котейка моего брата!',
       'вампир': "Прячься",
       'летит':"Прикольно, правда?",
       'ест':"Ты тоже иди покушай",
       'наелся':"На самом деле он бы еще поел..."}

photo= {'спит': "https://zagony.ru/uploads/posts/2014-12/1420023271_2.jpg" ,
        'феникс': 'https://sun9-37.userapi.com/impg/q1BR3GdX4tgas4HcuBkobWejhu8On0g2GjuIZw/kZ4HZ0r7EAQ.jpg?size=1620x2160&quality=96&sign=0ed33dfd42743901fac457ddc6f4feb8&type=album',
        'вампир': "https://medialeaks.ru/wp-content/uploads/2017/10/1-8-500x500.jpg",
        'летит':"https://sun9-78.userapi.com/impg/88P8ehYFooObIqR48Ee5W_cJwIKiIMcDhhm4BA/6pIy90ODKz8.jpg?size=610x610&quality=96&sign=73065fd55961477677196d14cfe70349&type=album",
        'ест':"https://pbs.twimg.com/media/Eqv_nUdXMAApd2i.jpg",
        'наелся':"https://funart.pro/uploads/posts/2021-07/1625805370_8-funart-pro-p-samaya-tolstaya-koshka-zhivotnie-krasivo-f-8.jpg"}

predictions= ('Eсли Вы проявите инициативу, успех не заставит себя ждать.',
              'Ваши надежды и планы сбудутся сверх всяких ожиданий.',
              'Готовьтесь к романтическим приключениям.',
              'В этом месяце ночная жизнь для вас.',
              'Вам пора отдохнуть.',
              'Вам предлагается мечта всей жизни. Скажите да!',
              'Вас ждет приятный сюрприз.',
              'Ваши надежды и планы сбудутся сверх всяких ожиданий.',
              'Время – ваш союзник, лучше отложить принятие важного решения хотя бы на день.',
              'Время и терпение,  вас ждут много сюрпризов!',
              'Время осушит все слезы и исцелит все раны.',
              'Не жди чуда – чуди сам.',
              'Мир принадлежит тому, кто ему рад.',
              'Поздравляем! Вы находитесь на верном пути.',
              'Покорив одну гору, начинай штурмовать другую...',
              'Прилив энергии поможет Вам справиться с большим объемом незапланированных работ.',
              'Примите то, что вы не можете изменить, и вы будете чувствовать себя лучше.',
              'Природа, время и терпение - три великих врача.',
              'Пришло время действовать!',
              'Пришло время закончить старое и начать новое.')


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Привет")
    keyboard.row("Спит")
    keyboard.row("Феникс")
    keyboard.row("Вампир")
    keyboard.row("Летит")
    keyboard.row("Ест")
    keyboard.row("Наелся")
    keyboard.row("/day")
    keyboard.row("/fortunacat")
    keyboard.row("/help")
    bot.send_message(message.chat.id, 'Поприветствуй котиков :з', reply_markup=keyboard)



@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Выбери нужного тебе котика в кнопках, либо отправь:\n'\
                                      '"Спит" - появится спящий котик;\n'\
                                      '"Вампир" - появится котик Дракула;\n'\
                                      '"Летит" - появится летающий котик;\n'\
                                      '"Ест" - появится кушающий котик;\n'\
                                      '"Наелся" - появится котик, который уже покушал;\n\n'\
                                      '"/day" - узнай, какой ты котик сегодня'\
                                      '"/fortunacat" - Кошка-Гадалка предскажет твое будущее'\
                                      'Удачи!')


@bot.message_handler(commands=['day'])
def start_message(message):
    bot.send_message(message.chat.id, 'О, ты хочешь узнать какой ты сегодня котик? Хм, дай-ка мне сначала подумать...]')
    bot.send_photo(message.chat.id, get(photo.get(random.choice(list(photo.keys()) ) ) ).content)


@bot.message_handler(commands=['fortunacat'])
def start_message(message):
    bot.send_message(message.chat.id, 'Коn-Гадалка приготовила для тебя предсказание!')
    bot.send_message(message.chat.id, predictions[random.randint(0,19)])
    bot.send_photo(message.chat.id, get("https://lh3.googleusercontent.com/proxy/7vee6Fi6CEaqWdZEc8o1IO_xd_2zsQhhd5urgPqmK_0W90igUeKL6r_2uWKUIxh4PPWKTZ3pV-R0MOiOTKHBRiGz8VN7X7Mk7GItO-YgxPjh6v9Hs9iA").content)


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, 'Привет! А я тут котиков показываю. Нажми на кнопочку "/help", если тебе нужна помощь, либо выбери, какого котика ты хочешь посмотреть.')
    elif message.text.lower() in cats:
        bot.send_message(message.chat.id, cats.get( message.text.lower() ) )
        bot.send_photo(message.chat.id, get( photo.get( message.text.lower()) ).content)
    else :
        bot.send_message(message.chat.id, "Если тебе требуется помощь, нто напиши /help." )


bot.polling()