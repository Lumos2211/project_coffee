from aiogram import F, Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


from utils import search_rating
from database.database import add_to_database
import keybords.keybords as kb

import logging
logger = logging.getLogger(__name__)


router_2 = Router()


class Register_2(StatesGroup):
    year = State()
    rating = State()
    genres = State()
    limit= State()



@router_2.message(F.text == "О нас")
async def register(message: Message):
    logger.info('start hendler about')
    await message.answer('', reply_markup=ReplyKeyboardRemove())