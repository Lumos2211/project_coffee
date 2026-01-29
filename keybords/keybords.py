from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
                            InlineKeyboardMarkup, InlineKeyboardButton)

keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='Меню')],
        [KeyboardButton(text='График мероприятий')],
        [KeyboardButton(text='О нас')]],
            resize_keyboard=True,
            input_field_placeholder='Выберите пункт меню...')


catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Продолжим поиск?', callback_data='reset')]])

