import asyncio

from aiogram import executor

from loader import dp
import middlewares, handlers
from utils.misc.backup import upload_backup
from utils.scheduler import scheduler
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)
    await upload_backup()
    asyncio.create_task(scheduler())
    pass


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
