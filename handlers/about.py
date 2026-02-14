from aiogram import F, Router
from aiogram.types import Message

import keybords.keybords as kb
import os

import logging
logger = logging.getLogger(__name__)


router = Router()


@router.message(F.text == "О нас")
async def about_handler(message: Message):
    logger.info('start handler about')
    # Читаем текст из файла
    file_path = os.path.join('utils', 'about_us.txt')
    with open(file_path, 'r', encoding='utf-8') as file:
        text_content = file.read()
    
    # Отправляем текст пользователю
    await message.answer(text_content)