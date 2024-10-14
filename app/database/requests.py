from app.database.models import User, Task
from app.database.models import async_session  # подключение к б.д
from sqlalchemy import select, delete


async def set_user(tg_id: int) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:  # если пользователь не зарегестрировался 
            session.add(User(tg_id=tg_id))
            await session.commit()  # сохраняю действия


async def get_tasks(tg_id: int) -> str:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))  # Мы каждый раз проверяем, id пользователя, для того, чтобы чужие задачи не лежали у пользователя в б.д
        tasks = await session.scalars(select(Task).where(Task.user == user.id))
        return tasks


async def add_task(tg_id: int, task: str) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        session.add(Task(task=task, user=user.id))
        await session.commit()
        
        
async def del_task(task_id: int) -> None:
    async with async_session() as session:
        await session.execute(delete(Task).where(Task.id == task_id))
        await session.commit()

