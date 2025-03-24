import redis.asyncio as redis


async def get_connection(url: str):
    connection = await redis.Redis.from_url(url)
    return connection
