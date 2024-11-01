import uvicorn, os

from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.api.endpoints.files import file_router
from app.core.config import settings
from app.db.database import async_delete_tables, async_create_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    await async_create_tables()
    print("База готова")
    yield
    await async_delete_tables()
    print("База очищена")

app = FastAPI(lifespan=lifespan)

app.include_router(file_router)

if __name__ == "__main__":
    num_cores = os.cpu_count()
    uvicorn.run("main:app", host=settings.PROJECT_HOST, 
                port=settings.PROJECT_PORT)