from typing import Any, Sequence, Optional, List

from sqlalchemy import select, delete, update
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import (AsyncEngine, AsyncSession, 
                                   async_sessionmaker, create_async_engine)
from .base import Base


class DatabaseContext:
    def __init__(self, engine: AsyncEngine, session_maker: async_sessionmaker[AsyncSession]):
        self.engine = engine
        self.session_maker = session_maker

    @staticmethod
    async def create(connection_string: str) -> type["DatabaseContext"]:
        engine = DatabaseContext._create_engine(connection_string, True)
        session_maker = await DatabaseContext._create_session_maker(engine)
        await DatabaseContext._create_tables(engine)
        return DatabaseContext(engine, session_maker)

    @staticmethod
    async def _create_tables(engine: AsyncEngine):
        async with engine.begin() as conn:
             await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    def _create_engine(connection_string: str, echo: bool = False) -> AsyncEngine:
        engine = create_async_engine(connection_string, echo=echo)
        return engine

    @staticmethod
    async def _create_session_maker(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        session_maker = async_sessionmaker(bind=engine)
        return session_maker
    
    async def add(self, entity: Base) -> None:
        async with self.session_maker() as session:
            session.add(entity)
            await session.commit()

    async def get(self, entity_type: type, condition: Any, relationships: List[Any] = []) -> Optional[Base]:
        query = select(entity_type).where(condition)
        if relationships:
            query = query.options(*[joinedload(rel) for rel in relationships])
        async with self.session_maker() as session:
            result = await session.execute(query)
            entity = result.scalars().first()
            return entity
        
    async def get_all(self, entity_type: type, condition: Any, relationships: List[Any] = []) -> Sequence[Base]:
        query = select(entity_type).where(condition)
        if relationships:
            query = query.options(*[joinedload(rel) for rel in relationships])
        async with self.session_maker() as session:
            result = await session.execute(query)
            entity = result.scalars().all()
            return entity
        
    async def delete(self, entity_type: type, condition: Any) -> None:
        query = delete(entity_type).where(condition)
        async with self.session_maker() as session:
            await session.execute(query)
            await session.commit()
    
    async def update(self, entity_type: type, condition: Any, **kwargs) -> None:
        query = update(entity_type).where(condition).values(kwargs)
        async with self.session_maker() as session:
            await session.execute(query)
            await session.commit()
    
