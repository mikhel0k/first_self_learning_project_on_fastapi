from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core import db_helper
from core.schemas import AuthorSchema, AuthorCreate, AuthorUpdate, AuthorWithBooksSchema
from .crud import authorCRUD

router = APIRouter(prefix="/authors", tags=["authors"])


@router.get(
    "/",
    response_model=List[AuthorSchema],
)
async def get_all_authors(
        session: AsyncSession = Depends(db_helper.get_session),
) -> List[AuthorSchema]:
    authors = await authorCRUD.get_all_authors(
        session=session,
    )
    return authors


@router.get(
    "/{author_id}/",
    response_model=AuthorSchema,
)
async def get_author(
        author_id: int,
        session: AsyncSession = Depends(db_helper.get_session),
) -> AuthorSchema:
    author = await authorCRUD.get_author(
        author_id=author_id,
        session=session,
    )
    return author


@router.get(
    "/{author_id}/with_books/",
    response_model=AuthorWithBooksSchema,
)
async def get_author_books(
        author_id: int,
        session: AsyncSession = Depends(db_helper.get_session),
) -> AuthorWithBooksSchema:
    author = await authorCRUD.get_author_with_books(
        author_id=author_id,
        session=session,
    )
    return author


@router.post(
    "/",
    response_model=AuthorSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_author(
        created_author: AuthorCreate,
        session: AsyncSession = Depends(db_helper.get_session),
) -> AuthorSchema:
    author = await authorCRUD.create_author(
        created_author=created_author,
        session=session,
    )
    return author


@router.patch(
    "/{author_id}/",
    response_model=AuthorSchema,
)
async def update_author(
        author_id: int,
        updated_author: AuthorUpdate,
        session: AsyncSession = Depends(db_helper.get_session),
) -> AuthorSchema:
    author = await authorCRUD.update_author(
        author_id=author_id,
        updated_author=updated_author,
        session=session,
    )
    return author


@router.delete(
    "/{author_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_author(
        author_id: int,
        session: AsyncSession = Depends(db_helper.get_session),
) -> None:
    await authorCRUD.delete_author(
        deleted_author_id=author_id,
        session=session,
    )
