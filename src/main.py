from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from services.database import DatabaseContext
from services.redis import RedisService
from services.parsing.parsers import FreelanceruParser

from handlers.user import start, commands, callbacks, mail
from middlewares import DatabaseMiddleware
from utils.config import TOKEN, DB_CONNECTION_STRING, REDIS_URL

import asyncio
import logging


async def main():
	dp = Dispatcher(storage=RedisStorage.from_url(REDIS_URL))
	bot = Bot(token=TOKEN)
	scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
	
	dp.include_router(start.router)
	dp.include_router(callbacks.router)
	dp.include_router(commands.router)

	dp.update.middleware(DatabaseMiddleware())

	scheduler.add_job(mail.send_mail, trigger="interval", seconds=10, kwargs={ "bot": bot,
																		   	   "parser": FreelanceruParser(),
																		   	   "context": await DatabaseContext.create(DB_CONNECTION_STRING),
																			   "redis": RedisService(REDIS_URL) })
	scheduler.start()

	logging.basicConfig(level=logging.DEBUG)
	await dp.start_polling(bot)

if __name__ == "__main__":
	try:
		asyncio.run(main())
	except (KeyboardInterrupt):
		print("Bot closing")
		
