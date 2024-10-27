import uvicorn

from fastapi import FastAPI
from app.api.endpoints.files import file_router

app = FastAPI()

app.include_router(file_router)

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
