import logging

import data as data
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler

from aiogram.dispatcher.middlewares import BaseMiddleware


class Basic(BaseMiddleware):
    # 1
    async def on_pre_process_update(self, update: types.update, data: dict):
        logging.info('==New==')
        logging.info('1. Pre process update')
        data["middleware_data"] = "pre_process_update"
        if update.message:
            user = update.message.from_user.id
        elif update.callback_query:
            user = update.callback_query.from_user.id
        else:
            return

        # if user in banned_users:
        #    raise CancelHandler()

    # 2
    async def on_process_update(self, update: types.Update, data: dict):
        logging.info(f"2. Process update, {data=}")

    # 3
    async def on_pre_process_message(self, message: types.Message, data: dict):
        logging.info(f"3. Pre process message, {data=}")

    # 4

    # 5
    async def on_process_message(self, message: types.Message, data: dict):
        logging.info(f"5. Process message, {data=}")
        data["middleware_data"] = "Handler"

    # 6

    # 7
    async def on_post_process_message(self, message: types.Message, data_from_handler, data: dict):
        logging.info(f"7. Post process message,\n{data}, \n{data_from_handler=}")

    async def on_pre_process_callback_query(self, query: types.CallbackQuery, data: dict):
        await query.answer()
