import asyncio
from aiogram.fsm.storage.memory import MemoryStorage

from aiogram import Bot, Dispatcher

from config_data.confing import BOT_TOKEN
from handlers.handler_start import start_router
from handlers.handler_about import about_router

import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


async def main():
    '''Основная функция инициализации и запуска Telegram бота'''
    bot = Bot(BOT_TOKEN)

    dp = Dispatcher(storage = MemoryStorage)
    dp.include_router(start_router)
    dp.include_router(about_router)
    

    await dp.start_polling(bot)

if __name__ == "__main__":
     asyncio.run(main())
    