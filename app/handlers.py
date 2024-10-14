from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery


from config import COMMANDS
import app.database.requests as rq
import app.keyboards as kb
import app.states as st
import app.functions as ft


router = Router()  # обрабатывает входящие сообщения


@router.message(CommandStart())
async def cmd_main(message: Message) -> str:
    await rq.set_user(message.from_user.id)
    await message.answer("Добро пожаловать в Todo бота!\nЕсли вам нужна помощь по боту нажмите на кнопку снизу", 
                         reply_markup=await kb.help_keyboard())
     

@router.callback_query(F.data == "help")
async def callback_help(callback: CallbackQuery):
    await callback.answer("Да здравствуют команды!")
    await callback.message.answer("Снизу представлены команды бота:",
                                  reply_markup=await kb.inline_commands())

    

@router.callback_query(F.data == "add_task")
async def add_task_step_first(callback: CallbackQuery, state: st.FSMContext):
    await state.set_state(st.Tasks.task)
    await callback.message.answer("Введите задачу:")
    

@router.message(st.Tasks.task)
async def add_task_step_second(message: CallbackQuery, state: st.FSMContext):
    await state.update_data(task=message.text)
    data = await state.get_data()
    await rq.add_task(message.from_user.id, data["task"])
    await message.reply("Задача успешно добавлена!\nПоказать ваши задачи?",
                        reply_markup=await kb.yes_no_keyboard())
    await state.clear() 
    
     
     
@router.callback_query(F.data == ("show_tasks"))
async def show_tasks(callback: CallbackQuery):
    await callback.answer("Ваши задачки!")
    str_tasks = ""
    tasks = await rq.get_tasks(callback.from_user.id)
    if hasattr(tasks, "__iter__"):
        for task in tasks:
            str_tasks += f"\t-- {task.task}\n"
        if not str_tasks.replace("\t-- \n", "") == "":
            await callback.message.answer(f"Ваши задачи:\n{str_tasks}\n• Если хотите что-то сделать нажмите на клавиатуру ниже:", 
                reply_markup=await kb.inline_commands())   
        else:
            await callback.message.answer("У вас еще нет задач, если хотите добавить, нажмите кнопку ниже", 
                                reply_markup=await kb.add_keyboard()) 
    

# при пустом списке дел все равно выводит нажмите на задачу
@router.callback_query(F.data == ("del_task"))
async def del_task_step_first(callback: CallbackQuery):
    await callback.answer("")
    await callback.message.answer("Нажмите на задачу, чтобы выполнить ее", 
                                  reply_markup=await kb.del_task(callback.from_user.id))


@router.callback_query(F.data.startswith("task_"))
async def del_task_step_second(callback: CallbackQuery):
    await callback.answer("Удаляем задачу")
    await rq.del_task(callback.data.split("_")[1])  # удаление задачи
    await callback.message.answer("Задача выполнена, поздравляю!\nОтобразить ваши задачи?", 
                                  reply_markup=await kb.yes_no_keyboard())
    
    
    
@router.callback_query(F.data == "Да")
async def cmd_yes(callback: CallbackQuery):
    await callback.answer("Отличный выбор!")
    await show_tasks(callback)  
    
    
    
@router.callback_query(F.data == "Нет")
async def cmd_no(callback: CallbackQuery):
    await callback.answer("Неплохой выбор!")
    await callback.message.answer("Что хотите сделать дальше?\n Нажмите кнопки на клавиатуре", 
                                  reply_markup=await kb.inline_commands())
    
    
    