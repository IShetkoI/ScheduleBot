from loader import dp
from aiogram import types


@dp.message_handler(commands='give_me')
async def give_me(message: types.Message):
    args = message.get_args()
    await dp.bot.delete_mesage(message.chat.id, message.message_id)
    await message.answer(f'Отправляю {args}')
