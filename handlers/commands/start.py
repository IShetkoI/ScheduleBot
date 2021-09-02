from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ParseMode
from aiogram.utils.markdown import text, bold

from keyboards.keyboards_scheduled import choose_group_kb
from loader import dp
from utils.misc import rate_limit


@rate_limit(5, key="start")
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.delete()
    await message.answer(text=text(bold("Выберите группу:")),
                         parse_mode=ParseMode.MARKDOWN,
                         reply_markup=choose_group_kb())
