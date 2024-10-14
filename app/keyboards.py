from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, 
                          ReplyKeyboardMarkup, KeyboardButton)

from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from app.database.requests import get_tasks, add_task
from config import COMMANDS



async def inline_commands() -> str:
    keyboard = InlineKeyboardBuilder()
    for command in COMMANDS.strip().split("\n"):
        command_with_slise = command[:command.index("-")]
        description = command[command.index("-"):]
        keyboard.add(InlineKeyboardButton(text=f"{command_with_slise}\n{description}", 
                                          callback_data=f"{command_with_slise.replace(' ', '').replace('/', '')}"))
    return keyboard.adjust(2).as_markup()


async def commands() -> str:
    keyboard = KeyboardBuilder()
    for command in COMMANDS.strip().split("\n"):
        command_with_slise = command[:command.index("-")]
        description = command[command.index("-"):]
        keyboard.add(KeyboardButton(text=f"{command_with_slise}\n{description}", 
                                          callback_data=f"{command_with_slise.replace(' ', '').replace('/', '')}"))
    return keyboard.adjust(2).as_markup().resize_keyboard()


async def help_keyboard() -> str:
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Команды бота", callback_data="help"))
    return keyboard.adjust(2).as_markup()


async def del_task(tg_id: int) -> str:
    keyboard = InlineKeyboardBuilder()
    tasks = await get_tasks(tg_id)
    for task in tasks:
        keyboard.add(InlineKeyboardButton(text=task.task, callback_data=f"task_{task.id}"))
    return keyboard.adjust().as_markup()


async def add_keyboard() -> int:
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="add_task", callback_data="add_task"))
    return keyboard.as_markup()


async def yes_no_keyboard() -> str:
    keyboard = InlineKeyboardBuilder()
    for word in ["Да", "Нет"]:
        keyboard.add(InlineKeyboardButton(text=word, callback_data=word))
    return keyboard.adjust(2).as_markup()

