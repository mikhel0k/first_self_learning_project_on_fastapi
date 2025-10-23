from fastapi import Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase

from core.database import db_helper


def get_item_by_id(model: type[DeclarativeBase]):
    async def dependency(
            item_id: int,
            db: AsyncSession = Depends(db_helper.get_session),
    ) -> DeclarativeBase:
        result = await db.execute(select(model).where(model.id == item_id))
        item = result.scalar_one_or_none()

        if not item:
            raise HTTPException(
                404,
                f"{model.__name__.title()} with {item_id} id does not found"
            )
        return item
    return dependency
