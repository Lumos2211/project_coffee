from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

import logging
logger = logging.getLogger(__name__)

import keybords.keybords as kb


router_0 = Router()

@router_0.message(CommandStart())
async def cmd_start(message: Message):
    logger.info('Получено сообщение с запросом')
    telegram_id = message.from_user.id
    username = message.from_user.username
    await message.answer(f"Привет, {telegram_id}/{username}! \n🔍 Для поиска используй кнопки ниже", reply_markup=kb.keyboard)