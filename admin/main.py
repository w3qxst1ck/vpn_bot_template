import asyncio
from asyncio.log import logger

import aiogram as io
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand, BotCommandScopeDefault
from config import BOT_TOKEN
from database.database import create_db
from routers.router import router


async def set_commands(bot: io.Bot):
    """Перечень команд для бота"""
    commands = [
        BotCommand(command="start", description="Запуск бота"),
        BotCommand(command="help", description="Справочная информация")
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def start_bot() -> None:
    """Запуск бота"""
    bot = io.Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await set_commands(bot)

    storage = MemoryStorage()
    dispatcher = io.Dispatcher(storage=storage)

    dispatcher.include_routers(router)

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    logger.info("Запуск бота...")
    create_db()
    asyncio.run(start_bot())
