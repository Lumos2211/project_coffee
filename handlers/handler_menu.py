from aiogram import F, Router
from aiogram.types import Message

import keybords.keybords as kb
import os

import logging

from utils.parse_yandex import responce_func
logger = logging.getLogger(__name__)


menu_router = Router()


@menu_router.message(F.text == "Меню")
async def menu_handler(message: Message):
    logger.info('start handler menu')
    menu_items = responce_func()

    # Форматируем текст
    menu_text = "🍽️ *МЕНЮ Imok Coffee X Friends*\n"
    menu_text += "═════════════════════\n\n"
    
    for i, item in enumerate(menu_items, 1):
        menu_text += f"*{i}.* {item}\n"
    
    menu_text += f"\nВсего позиций: *{len(menu_items)}*"
    
    # Отправляем
    await message.answer(menu_text, parse_mode="Markdown")