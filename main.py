from fastapi import FastAPI
from contextlib import asynccontextmanager

from core import db_helper, BaseModel
from core import api_v1_router


@asynccontextmanager
async def lifespan(app: FastAPI):

    yield

app = FastAPI(lifespan=lifespan)
app.include_router(api_v1_router)
