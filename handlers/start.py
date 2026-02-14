from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

import logging
logger = logging.getLogger(__name__)

import keybords.keybords as kb


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    logger.info('start bot')
    username = message.from_user.username
    await message.answer(f"Привет, {username}! \n🔍 Для поиска используй кнопки ниже", reply_markup=kb.keyboard)