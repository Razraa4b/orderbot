from typing import Any, List
import redis.asyncio as redis


async def set(conn: redis.Redis, key: str, value: Any, expire_time: int = None) -> None:
    async with conn.pipeline(transaction=True) as pipe:
        await pipe.set(key, value, expire_time)
        await pipe.execute()

async def get(conn: redis.Redis, key: str) -> Any:
    async with conn.pipeline(transaction=True) as pipe:
        await pipe.get(key)
        return await pipe.execute()

async def delete(conn: redis.Redis, key: str) -> None:
    async with conn.pipeline(transaction=True) as pipe:
        await pipe.delete(key)
        await pipe.execute()

async def push(conn: redis.Redis, key: str, new_items: List[Any]) -> None:
    async with conn.pipeline(transaction=True) as pipe:
        await pipe.rpush(key, *new_items)
        await pipe.execute()

async def set_expire(conn: redis.Redis, key: str, expire_time: int):
    async with conn.pipeline(transaction=True) as pipe:
        await pipe.expire(key, expire_time)
        await pipe.execute()

async def lrange(conn: redis.Redis, key: str, start: int, end: int) -> List:
    async with conn.pipeline(transaction=True) as pipe:
        await pipe.lrange(key, start, end)
        return await pipe.execute()
