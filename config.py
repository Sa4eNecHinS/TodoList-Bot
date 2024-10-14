TOKEN="7553915687:AAF9Jyoj_JpDUGcreMWma8Tnw9UJwEMX_cI"
COMMANDS="\n/help - информация о командах бота\n" + \
          "/add_task - добавить задачу\n" + \
          "/del_task  - удалить задачу\n" + \
          "/show_tasks - показать все задачи\n"
DB_URL="sqlite+aiosqlite:///db.sqlite3"


# for command in COMMANDS.strip().split("\n"):
#         command_with_slise = command[:command.index("-")]
#         description = command[command.index("-"):]
#         callback_data = command_with_slise.replace('/', '')
#         print(f"{callback_data}{description}")


