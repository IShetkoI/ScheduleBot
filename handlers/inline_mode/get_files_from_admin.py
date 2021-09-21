from aiogram import types

from data import config
from loader import dp
from utils.misc.backup import load_backup


@dp.message_handler(content_types=['document'])
async def get_file_from_admin(message: types.Message):
    if message.from_user.id == 410249555:
        name = message.caption[:message.caption.find('\n')]
        category = message.caption[message.caption.find('\n')+1:]
        print(name, category)
        temp = {name: [message.message_id, category, message.document.file_name]}
        config.lib.update(temp)
        config.lib = sorted(config.lib.items(), key=lambda x: x[0])
        config.lib = dict(config.lib)
        await load_backup()
