import sqlite3
import datetime

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
    await message.answer(str(datetime.datetime.now()))
