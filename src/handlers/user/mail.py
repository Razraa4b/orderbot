from typing import List
from datetime import datetime
from dateutil.relativedelta import relativedelta

from aiogram import Bot

from services.redis import RedisService
from services.database.models import User, UserBotSettings
from services.database import DatabaseContext
from services.parsing import Order, Parser


# Parses the data and then mail it
async def send_mail(bot: Bot, parser: Parser, context: DatabaseContext, redis: RedisService):
    await redis.connect()
    
    # select only new orders
    now = datetime.now()
    orders = []
    for order in await parser.parse():
        difference = relativedelta(now, order.publish_time)
        if (difference.years == 0 and
            difference.months == 0 and
            difference.days == 0 and
            difference.hours == 0 and
            difference.minutes < 30):
            orders.append(order)

    
    users_settings: List[UserBotSettings] = await context.get_all(UserBotSettings, UserBotSettings.is_active, [UserBotSettings.user])

    for user_settings in users_settings:
        user: User = user_settings.user

        viewed_links = await redis.lrange(user.telegram_id, 0, -1)

        if not viewed_links:
            new_links = list(map(lambda o: o.link, orders))
            await redis.push(user.telegram_id, new_links)
            await redis.expire(user.telegram_id, 1800)

            message = "New orders"
            for order in orders:
                message += f"\n\tTitle: \"{order.title}\", Link: {order.link}"
            await bot.send_message(user.telegram_id, message)
        else:
            # convert to normal string from byte string
            viewed_links = list(map(lambda x: x.decode("utf-8"), viewed_links))
            
            new_orders = []
            for order in orders:
                if order.link not in viewed_links:
                    new_orders.append(order)

            if new_orders:
                new_links = list(map(lambda o: o.link, new_orders))
                await redis.push(user.telegram_id, new_links)

                message = "New orders"
                for order in new_orders:
                    message += f"\n\tTitle: \"{order.title}\", Link: {order.link}"
                await bot.send_message(user.telegram_id, message)