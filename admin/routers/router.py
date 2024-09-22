from aiogram import Router, types
from aiogram.filters import Command


router = Router()


@router.message(Command("start"))
async def start_handler(message: types.Message) -> None:
    """Start message"""
    await message.answer("Hello!")


@router.message(Command("help"))
async def start_handler(message: types.Message) -> None:
    """Help message"""
    await message.answer("Справочная информация бота администратора")