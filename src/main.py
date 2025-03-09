from aiogram import Bot, Dispatcher

from handlers.user import start, commands, callbacks
from middlewares import DatabaseMiddleware
from utils.config import TOKEN

import asyncio
import logging


async def main():
	dp = Dispatcher()
	bot = Bot(token=TOKEN)

	dp.include_router(start.router)
	dp.include_router(callbacks.router)
	dp.include_router(commands.router)

	dp.update.middleware(DatabaseMiddleware())

	logging.basicConfig(level=logging.DEBUG)
	await dp.start_polling(bot)

if __name__ == "__main__":
	try:
		asyncio.run(main())
	except (KeyboardInterrupt):
		print("Bot closing")
		
