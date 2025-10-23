from typing import List

from fastapi import Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from core import Author
from core.schemas import AuthorSchema, AuthorCreate, AuthorUpdate
from ..dependencies import get_item_by_id


class AuthorCRUD:
    def __init__(self):
        self.get_item_by_id = get_item_by_id(Author)

    async def get_authors(
            self,
            session: AsyncSession
    ) -> List[AuthorSchema]:
        stmt = select(Author).order_by(Author.id)
        result = await session.execute(stmt)
        authors = result.scalars().all()

        return [AuthorSchema.model_validate(author) for author in authors]

    async def get_author(
            self,
            session: AsyncSession,
            author_id: int,
    ) -> AuthorSchema:
        author = await self.get_item_by_id(author_id, session)

        return AuthorSchema.model_validate(author)

    async def get_author_with_books(
            self,
            session: AsyncSession,
            author_id: int,
    ):
        stmt = select(Author).options(selectinload(Author.books)).where(Author.id == author_id)
        result = await session.execute(stmt)
        author = result.scalar_one_or_none()

        if not author:
            raise HTTPException(
                404,
                detail=f"Author with {author_id} id does not found"
            )

        return AuthorSchema.model_validate(author)

    async def create_author(
            self,
            session: AsyncSession,
            created_author: AuthorCreate,
    ) -> AuthorSchema:
        author = Author(**created_author.model_dump())

        session.add(author)
        await session.commit()
        await session.refresh(author)

        return AuthorSchema.model_validate(author)

    async def update_author(
            self,
            session: AsyncSession,
            author_id: int,
            updated_author: AuthorUpdate
    ) -> AuthorSchema:
        author = await self.get_item_by_id(author_id, session)

        updated_author = updated_author.model_dump(exclude_unset=True)
        for key, value in updated_author.items():
            setattr(author, key, value)

        await session.commit()
        await session.refresh(author)
        return AuthorSchema.model_validate(author)

    async def delete_author(
            self,
            session: AsyncSession,
            deleted_author_id: int
    ) -> None:
        author = await self.get_item_by_id(deleted_author_id, session)

        await session.delete(author)
        await session.commit()
