from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from starlette import status

from core import db_helper
from core.schemas import ReviewSchema, ReviewCreate, ReviewUpdate
from .crud import reviewCRUD


router = APIRouter(prefix="/reviews", tags=["reviews"])

@router.get(
    "/",
    response_model=List[ReviewSchema],
)
async def get_all_reviews(
        session: AsyncSession = Depends(db_helper.get_session)
) -> List[ReviewSchema]:
    reviews = await reviewCRUD.get_all_reviews(
        session=session
    )
    return reviews


@router.get(
    "/{review_id}/",
    response_model=ReviewSchema,
)
async def get_review_by_id(
        review_id: int,
        session: AsyncSession = Depends(db_helper.get_session),
):
    review = await reviewCRUD.get_review_by_id(
        review_id=review_id,
        session=session
    )
    return review


@router.post(
    "/",
    response_model=ReviewSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_review(
        created_review: ReviewCreate,
        session: AsyncSession = Depends(db_helper.get_session),
) -> ReviewSchema:
    review = await reviewCRUD.create_review(
        created_review=created_review,
        session=session
    )
    return review


@router.patch(
    "/{review_id}/",
    response_model=ReviewSchema,
)
async def update_review(
        review_id: int,
        updated_review: ReviewUpdate,
        session: AsyncSession = Depends(db_helper.get_session)
) -> ReviewSchema:
    review = await reviewCRUD.update_review(
        review_id=review_id,
        updated_review=updated_review,
        session=session
    )
    return review


@router.delete(
    "/{review_id}/",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_review(
        review_id: int,
        session: AsyncSession = Depends(db_helper.get_session)
) -> None:
    await reviewCRUD.delete_review(
        review_id=review_id,
        session=session,
    )
