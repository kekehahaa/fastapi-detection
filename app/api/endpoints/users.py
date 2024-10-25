import os, shutil

from fastapi import APIRouter, UploadFile
from fastapi.responses import  FileResponse

user_router = APIRouter()

@user_router.post("/upload/file")
async def upload_video_file(file: UploadFile):
    file_location = os.path.join("/Users/kekehaha/python/detection/video2photo", file.filename)
    
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    return {"message": "Видео успешно загружено", "file_path": file_location}

@user_router.get("/drive/{file}")
async def get_file(file: str):
    some_file_path = "/Users/kekehaha/python/detection/video2photo/" 
    return FileResponse(os.path.join(some_file_path, file))

@user_router.get("/")
async def echo_answer():
    return {'message': 'hi'}