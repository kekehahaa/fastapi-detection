from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from app.core.config import settings

class Base(DeclarativeBase):
    pass

async_engine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=True,
    # pool_size=5,
    # max_overflow=10,
    # future=True
)

async_session_maker = async_sessionmaker(async_engine, class_=AsyncSession)

async def async_create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
async def async_delete_tables():
   async with async_engine.begin() as conn:
       await conn.run_sync(Base.metadata.drop_all)

async def get_async_session():
    async with async_session_maker() as session:
        yield session
        
