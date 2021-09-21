from data import config
from loader import dp


async def upload_backup():
    config.lib = {}
    lib_list = await dp.bot.forward_message(chat_id=-1001250101317, from_chat_id=-1001250101317, message_id=3561)
    config.lib = eval(lib_list.text)
    await lib_list.delete()


async def load_backup():
    await dp.bot.edit_message_text(text=config.lib, chat_id=-1001250101317, message_id=3561)
