import asyncio
from aiogram.fsm.storage.memory import MemoryStorage

from aiogram import Bot, Dispatcher

from config_data.confing import BOT_TOKEN
import handlers

import logging

from keybords.menu import set_main_menu
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


async def main():
    '''Основная функция инициализации и запуска Telegram бота'''
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(handlers.setup_routers())
    await set_main_menu(bot)
    await dp.start_polling(bot)

if __name__ == "__main__":
     asyncio.run(main())
    