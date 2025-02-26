from aiogram import Bot, Dispatcher

from handlers import start
from utils.config import TOKEN

import asyncio
import logging


async def main():
	dp = Dispatcher()
	bot = Bot(token=TOKEN)

	dp.include_router(start.router)

	logging.basicConfig(level=logging.DEBUG)
	await dp.start_polling(bot)

if __name__ == "__main__":
	asyncio.run(main())

