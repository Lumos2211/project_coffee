from aiogram import Bot
from aiogram.types import Message, BotCommand, BotCommandScopeDefault


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command='/start', description='Перезапустить бота'),
    ]
    await bot.set_my_commands(main_menu_commands, BotCommandScopeDefault())