from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy import String, BigInteger, ForeignKey

from config import DB_URL

engine = create_async_engine(url=DB_URL)  # создание Б.Д
async_session = async_sessionmaker(engine)  # подключние к Б.Д


class Base(AsyncAttrs, DeclarativeBase):
    # DeclarativeBase позволяет создавать классы совместимые с проверкой типов
    # AsyncAttrs позволяет с каждым классом работать асинхронно
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)  # уникальный индификатор каждой таблицы
    tg_id = mapped_column(BigInteger)


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    task: Mapped[str] = mapped_column(String(120))
    user: Mapped[int] = mapped_column(ForeignKey("users.id"))
    

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

