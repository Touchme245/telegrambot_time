from cmath import phase
import telebot
from telebot import types
from datetime import *

bot = telebot.TeleBot('5753725050:AAG2TEQzNKeDBFdiMexCtYUwSkq1Taws8HA')



@bot.message_handler(commands=['start'])
def start(message):
    mess = "Привет, я могу помочь тебе с расписанием на сегодня, пожалуйста, введи номер своей группы ( пока доступна только 101 )"
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    ned = datetime.isocalendar(datetime.now())
    if message.text == "101" and ned[1] % 2 == 0:
        b = ned[2]
        if b == 1: #понедельник
            mess = "Дискретная математика 9:00 - 10:30 ЛР ГУК Б-325\nДискретная математика 10:45 - 12:15 ЛР ГУК Б-325\nЛинейная алгебра и аналитическая геометрия 13:00 - 14:30 ПЗ 3-301\nМатематический анализ 14:45 - 16:15 ПЗ 3-131"
            bot.send_message(message.chat.id, mess, parse_mode='html')
        elif b == 2: #вторник
            mess = "Математический анализ 9:00 - 10:30 ЛК ГУК Б-649\nМатематический анализ 10:45 - 12:15 ЛК ГУК Б-649\nЛабораторная работа по информатике 14:00 - 19:00 IT-13\n"
            bot.send_message(message.chat.id, mess, parse_mode='html')
        elif b == 3: #среда
            mess = "Физическая культура 10:45 - 12:15 ПЗ\nФундаментальная информатика 13:00 - 14:30 ЛК ГУК В-221\nФундаментальная информатика 14:45 - 16:15 ЛК ГУК В-221\nФундаментальная информатика 16:30 - 18:00 ЛК ГУК В-221\n"
            bot.send_message(message.chat.id, mess, parse_mode='html')
        elif b == 4: #четверг
            mess = "Линейная алгебра и аналитическая геометрия 9:00 - 10:30 ЛК ГУК В-221\nДискретная математика 10:45 - 12:15 ЛК ГУК В-214\nВведение в авиационную и ракетно-космическую технику 13:00 - 14:30 ЛК ГУК В-221\nФизическая культура 14:45 - 16:15 ПЗ\n"
            bot.send_message(message.chat.id, mess, parse_mode='html')
        elif b == 5: #пятница
            mess = "ИНостранный язык 9:00 - 10:30 ПЗ Орш. Б-603\nИстория 10:45 - 12:15 ЛК Орш. В-505\nПравоведение 13:00 - 14:30 ЛК Орш. А-101\nИстория 14:45 - 16:15 ПЗ Орш. А-305\n"
            bot.send_message(message.chat.id, mess, parse_mode='html')
        elif b == 6: #суббота
            mess = "Выходной\n"
            bot.send_message(message.chat.id, mess, parse_mode='html')
        elif b == 7: #воскресенье
            mess = "Выходной\n"
            bot.send_message(message.chat.id, mess, parse_mode='html')
    if message.text == "101" and ned[1] % 2 != 0: #другая неделя
        b = ned[2]
        if b == 1: #понедельник
            mess = "Линейная алгебра и аналитическая геометрия 13:00 - 14:30 ПЗ 3-301\nМатематический анализ 14:45 - 16:15 ПЗ 3-131"
            bot.send_message(message.chat.id, mess, parse_mode='html')
        elif b == 2: #вторник
            mess = "Математический анализ 10:45 - 12:15 ЛК ГУК Б-649\nЛабораторная работа по информатике 14:00 - 19:00 IT-17\n"
            bot.send_message(message.chat.id, mess, parse_mode='html')
        elif b == 3: #среда
            mess = "Физическая культура 10:45 - 12:15 ПЗ\nФундаментальная информатика 13:00 - 14:30 ЛК ГУК Б-221\nФундаментальная информатика 14:45 - 16:15 ЛК ГУК Б-221\nФундаментальная информатика 16:30 - 18:00 ЛК ГУК Б-221\n"
            bot.send_message(message.chat.id, mess, parse_mode='html')
        elif b == 4: #четверг
            mess = "Линейная алгебра и аналитическая геометрия 9:00 - 10:30 ЛК ГУК В-221\nДискретная математика 10:45 - 12:15 ЛК ГУК В-214\nВведение в авиационную и ракетно-космическую технику 13:00 - 14:30 ЛК ГУК В-221\nФизическая культура 14:45 - 16:15 ПЗ\n"
            bot.send_message(message.chat.id, mess, parse_mode='html')
        elif b == 5: #пятница
            mess = "ИНостранный язык 9:00 - 10:30 ПЗ ОРШ. Б-605\nИстория 10:45 - 12:15 ЛК Орш. В-501\nПравоведение 13:00 - 14:30 ПЗ Орш. В-209\nИстория 14:45 - 16:15 ПЗ Орш. А-305\n"
            bot.send_message(message.chat.id, mess, parse_mode='html')
        elif b == 6: #суббота
            mess = "Выходной\n"
            bot.send_message(message.chat.id, mess, parse_mode='html')
        elif b == 7: #воскресенье
            mess = "Выходной\n"
            bot.send_message(message.chat.id, mess, parse_mode='html')




bot.polling(non_stop = True)