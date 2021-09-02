import sqlite3

from aiogram import types
from aiogram.types import ParseMode
from aiogram.utils.markdown import bold

from data import config
from handlers.schedule.get_schedule_list import get_schedule_list
from handlers.schedule.get_time_now import get_table_fourth, get_table_fifth
from loader import dp


@dp.message_handler(commands='week')
async def schedule_week(message: types.Message):
    await message.delete()
    conn = sqlite3.connect('data.sqlite')
    cursor = conn.cursor()
    message_text = ''
    if config.users[message.chat.username]['info']['group'] == '4':
        for i in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]:
            sql = "SELECT Time, {0} FROM '{1}'".format(i, (get_table_fourth(message.chat.username)))
            cursor.execute(sql)
            day_list = cursor.fetchall()
            if i == 'Monday':
                message_text += bold('Понедельник')+'\n\n' + get_schedule_list(day_list) + '\n'
            elif i == 'Tuesday':
                message_text += bold('Вторник')+'\n\n' + get_schedule_list(day_list) + '\n'
            elif i == 'Wednesday':
                message_text += bold('Среда')+'\n\n' + get_schedule_list(day_list) + '\n'
            if i == 'Thursday':
                message_text += bold('Четверг')+'\n\n' + get_schedule_list(day_list) + '\n'
            elif i == 'Friday':
                message_text += bold('Пятница')+'\n\n' + get_schedule_list(day_list) + '\n'
            elif i == 'Saturday':
                message_text += bold('Суббота')+'\n\n' + get_schedule_list(day_list) + '\n'

    else:
        for i in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]:
            sql = "SELECT Time, {0} FROM '{1}'".format(i, (get_table_fifth(message.chat.username)))
            cursor.execute(sql)
            day_list = cursor.fetchall()
            if i == 'Monday':
                message_text += bold('Понедельник')+'\n\n' + get_schedule_list(day_list) + '\n'
            elif i == 'Tuesday':
                message_text += bold('Вторник')+'\n\n' + get_schedule_list(day_list) + '\n'
            elif i == 'Wednesday':
                message_text += bold('Среда')+'\n\n' + get_schedule_list(day_list) + '\n'
            if i == 'Thursday':
                message_text += bold('Четверг')+'\n\n' + get_schedule_list(day_list) + '\n'
            elif i == 'Friday':
                message_text += bold('Пятница')+'\n\n' + get_schedule_list(day_list) + '\n'
            elif i == 'Saturday':
                message_text += bold('Суббота')+'\n\n' + get_schedule_list(day_list) + '\n'
    await message.answer(message_text, parse_mode=ParseMode.MARKDOWN, reply_markup=rating_keyboard())
