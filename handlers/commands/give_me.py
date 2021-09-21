from data import config
from loader import dp
from aiogram import types


@dp.message_handler(commands='give_me')
async def give_me(message: types.Message):
    args = message.get_args()
    await dp.bot.delete_message(message.chat.id, message.message_id)
    print(config.lib[args][0])
    print(config.lib[args])
    print(config.lib)

    await dp.bot.forward_message(chat_id=message.chat.id, from_chat_id=-1001250101317, message_id=config.lib[args][0])
