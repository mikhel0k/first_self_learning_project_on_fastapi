from fastapi import FastAPI
from contextlib import asynccontextmanager

from core import db_helper, BaseModel, authors_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)

    yield

app = FastAPI(lifespan=lifespan)
app.include_router(authors_router)
