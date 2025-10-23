from .authors import authors_router
from .reviews import views_router
from .books import books_router

from fastapi import APIRouter

api_v1_router = APIRouter(prefix="/v1")
api_v1_router.include_router(authors_router)
api_v1_router.include_router(views_router)
api_v1_router.include_router(books_router)

__all__ = ['api_v1_router']