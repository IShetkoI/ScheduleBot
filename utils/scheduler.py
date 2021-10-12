import asyncio
import sqlite3

import aioschedule
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from data import config
from handlers.schedule.get_schedule_list import get_schedule_list
from handlers.schedule.get_time_now import get_time, get_time_range, get_weekday, get_table_fourth, get_table_fifth
from loader import dp


# async def scheduler():
    # if get_time().weekday() != 6:
        # aioschedule.every().days.at("4:40").do(schedule_notification)
        # aioschedule.every().days.at("6:15").do(schedule_notification)
        # aioschedule.every().days.at("7:50").do(schedule_notification)
        # aioschedule.every().days.at("9:40").do(schedule_notification)
    # while True:
        # await aioschedule.run_pending()
        # await asyncio.sleep(1)


async def schedule_notification():

    conn = sqlite3.connect('data.sqlite')
    cursor = conn.cursor()
    sql = 'SELECT Time, {0} FROM "{1}" WHERE Time Like "{2}"'.format(get_weekday(), (get_table_fourth(1)),
                                                                         get_time_range())
    cursor.execute(sql)
    day_list = cursor.fetchall()
    message_text = get_schedule_list(day_list)
    if message_text == '':
        return
    else:
        keyboard = InlineKeyboardMarkup(row_width=1)
        bt1 = InlineKeyboardButton('Удаляй', callback_data='delete')
        keyboard.add(bt1)
        await dp.bot.send_message(chat_id=410249555, text=message_text, reply_markup=keyboard)


@dp.callback_query_handler()
async def delete_message(query: CallbackQuery):
    await query.message.delete()
