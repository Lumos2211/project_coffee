from aiogram.fsm.storage.memory import MemoryStorage

from aiogram import Bot, Dispatcher

from config_data.confing import BOT_TOKEN
from handlers.handler_start import start_router

import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


async def main_bot():
    '''Основная функция инициализации и запуска Telegram бота'''
    bot = Bot(BOT_TOKEN)

    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    dp.include_router(start_router)

    await dp.start_polling(bot)
    