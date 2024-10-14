import logging
import asyncio

from aiogram import Bot, Dispatcher
from app.handlers import router
from config import TOKEN
from app.database.models import async_main

bot = Bot(TOKEN)
dp = Dispatcher()

async def main() -> None:
    await async_main()
    dp.include_router(router)
    await dp.start_polling(bot)  # разрешение на отправление ботом запросы в телеграмм


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Finalization of work")



