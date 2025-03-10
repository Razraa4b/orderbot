from typing import List
from datetime import datetime
from dateutil.relativedelta import relativedelta

from aiogram import Bot

from services.database.models import User, UserBotSettings
from services.database import DatabaseContext
from services.parsing import Order, Parser


# Parses the data and then mail it
async def send_mail(bot: Bot, parser: Parser, context: DatabaseContext):
    orders = [order for order in await parser.parse()]
    users_settings: List[UserBotSettings] = await context.get_all(UserBotSettings, UserBotSettings.is_active, [UserBotSettings.user])

    # Collect the message about new orders
    orders_as_message = ""
    for order in orders:
        difference = relativedelta(datetime.now(), order.publish_time)
        print(f"{order.title} | {difference.hours}")
        if (difference.years == 0
            and difference.months == 0
            and difference.days == 0
            and difference.hours == 0
            and difference.minutes < 30):
            orders_as_message += f"Link: {order.link}, Title: {order.title}\n\n"

    for user_settings in users_settings:
        user: User = user_settings.user

        if orders_as_message != "":
            await bot.send_message(user.telegram_id, f"Parsed orders:\n{orders_as_message}")
