import asyncio
import sqlite3

import aioschedule
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data import config
from handlers.schedule.get_schedule_list import get_schedule_list
from handlers.schedule.get_time_now import get_time, get_time_range, get_weekday, get_table_fourth, get_table_fifth
from loader import dp


async def scheduler():
    aioschedule.every(4).hours.do(load_backup)
    aioschedule.every().day.at("23:40").do(reset_daily_reward)
    if get_time().weekday() != 6:
        aioschedule.every().days.at("7:45").do(schedule_notification)
        aioschedule.every().days.at("9:21").do(schedule_notification)
        aioschedule.every().days.at("10:56").do(schedule_notification)
        aioschedule.every().days.at("12:46").do(schedule_notification)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def reset_daily_reward():
    for key, items in config.users.items():
        config.users[key]['casino']['daily_reward'] = False


async def schedule_notification():
    if get_time_range() is not None:
        print('ok')
        conn = sqlite3.connect('data.sqlite')
        cursor = conn.cursor()

        for key, items in config.users.items():
            if config.users[key]['info']['group'] == '4':
                sql = 'SELECT Time, {0} FROM "{1}" WHERE Time Like "{2}"'.format(get_weekday(), (get_table_fourth(key)),
                                                                                 get_time_range())
            else:
                sql = 'SELECT Time, {0} FROM "{1}" WHERE Time Like "{2}"'.format(get_weekday(), (get_table_fifth(key)),
                                                                                 get_time_range())
            cursor.execute(sql)
            day_list = cursor.fetchall()
            message_text = get_schedule_list(day_list)
            if message_text == '':
                return
            else:
                keyboard = InlineKeyboardMarkup(row_width=1)
                bt1 = InlineKeyboardButton('Удаляй', callback_data=settings_callback.new(settings='settings', func='delete'))
                keyboard.add(bt1)
                await dp.bot.send_message(chat_id=config.users[key]['info']['chat_id'], text=message_text, reply_markup=keyboard)
