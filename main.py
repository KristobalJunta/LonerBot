#!/usr/bin/python3
# -*- coding: utf8 -*-

from fuzzywuzzy import process
import sqlite3
from config import config
from telebot import TeleBot, types


conn = sqlite3.connect(config.get('db'))
cur = conn.cursor()

cur.execute("SELECT * FROM voices;")
voices = cur.fetchall()

texts = [v[2] for v in voices]

bot = TeleBot(config.get('token'))


@bot.message_handler(commands=['help'])
def command_help(message):
    response = ''.join([
        'Первый войсостикерпак!\n',
        'Спасибо за голос @LonerNya, за материалы – @RpRICE\n',
        '\n',
        'https://github.com/KristobalJunta/LonerBot'
    ])
    bot.send_message(message.chat.id, response)


@bot.inline_handler(lambda query: len(query.query) > 0)
def handle_inline(query):
    print(query)
    try:
        result = process.extract(query.query, texts)
        result = list(filter(lambda x: x[1] > 60, result))

        result_voices = []
        for r in result:
            for v in voices:
                if v[2] == r[0]:
                    result_voices.append(v)

        response = []

        i = 1
        for v in result_voices:
            r = types.InlineQueryResultArticle(i, v[2], types.InputTextMessageContent(v[2]))
            response.append(r)
            i += 1

        print(result_voices)
        bot.answer_inline_query(query.id, response)
    except Exception as e:
        print(e)


bot.polling(none_stop=True, interval=0)
