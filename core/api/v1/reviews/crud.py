from typing import List

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import Review
from ..dependencies import get_item_by_id
from core.schemas import ReviewSchema, ReviewCreate, ReviewUpdate


class ReviewsCRUD:
    def __init__(self):
        self.get_item_by_id = get_item_by_id(Review)

    async def get_all_reviews(
            self,
            session: AsyncSession,
    ) -> List[ReviewSchema]:
        stmt = select(Review).order_by(Review.id)
        result = await session.execute(stmt)
        all_reviews = result.scalars().all()

        return [ReviewSchema.model_validate(review) for review in all_reviews]

    async def get_review_by_id(
            self,
            review_id: int,
            session: AsyncSession,
    ) -> ReviewSchema:
        result = await self.get_item_by_id(review_id, session)

        return ReviewSchema.model_validate(result)

    async def create_review(
            self,
            created_review: ReviewCreate,
            session: AsyncSession,
    ) -> ReviewSchema:
        review = Review(**created_review.model_dump())

        session.add(review)
        await session.commit()
        await session.refresh(review)

        return ReviewSchema.model_validate(review)

    async def update_review(
            self,
            review_id: int,
            updated_review: ReviewUpdate,
            session: AsyncSession,
    ) -> ReviewSchema:
        review = await self.get_item_by_id(review_id, session)

        for key, value in updated_review.model_dump(exclude_unset=True).items():
            setattr(review, key, value)

        await session.commit()
        await session.refresh(review)

        return ReviewSchema.model_validate(review)


    async def delete_review(
            self,
            review_id: int,
            session: AsyncSession,
    ) -> None:
        review = await self.get_item_by_id(review_id, session)

        await session.delete(review)
        await session.commit()


reviewCRUD = ReviewsCRUD()
