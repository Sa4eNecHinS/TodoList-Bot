# from aiogram.types import Message, CallbackQuery

# from config import COMMANDS
# import app.keyboards as kb
# import app.states as st
# import app.database.requests as rq


# async def cmd_help(txt_message: Message | CallbackQuery):
#     if txt_message == CallbackQuery:
#         await txt_message.message.answer(f"Ниже представленны команды бота:", 
#                                      reply_markup=await kb.inline_commands())
#     else:
#         await txt_message.answer(f"Ниже представленны команды бота: {COMMANDS}", 
#                             reply_markup=await kb.commands())
        
        
# async def cmd_del_task_step_first(txt_message: Message | CallbackQuery, state: st.FSMContext):
#     if txt_message:
#          await callback.message.answer("Нажмите на задачу, чтобы выполнить ее", 
#                                   reply_markup=await kb.del_task(callback.from_user.id))
#          await cmd_del_task_step_second(txt_message)
         

# async def cmd_del_task_step_second(callback: CallbackQuery):
#     await rq.del_task(callback.data.split("_")[1])
#     await callback.message.answer("Задача выполнена, поздравляю!\nОтобразить ваши задачи?", 
#                                   reply_markup=await kb.yes_no_keyboard())
        

# async def cmd_add_task(txt_message: Message | CallbackQuery):
#     if txt_message == CallbackQuery:
#         await txt_message.message.answer()
#     else:
#         await txt_message.answer()