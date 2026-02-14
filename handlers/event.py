from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

import logging
logger = logging.getLogger(__name__)

import keybords.keybords as kb


router = Router()

@router.message(CommandStart())
async def event(message: Message):
    logger.info('hendler event start')
    await message.answer(f"Привет, этот раздел пока в работе! \n🔍 Для поиска используй кнопки ниже", reply_markup=kb.keyboard)