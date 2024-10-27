from fastapi import APIRouter, UploadFile, HTTPException
from fastapi.responses import  FileResponse
from fastapi import status

from app.utils.files import upload_files_user, upload_files_link

file_router = APIRouter()

@file_router.post("/upload/video")
async def upload_video_file(files: list[UploadFile]):        
    files = await upload_files_user(files, "/Users/kekehaha/python/detection/video2photo/582858358/videos/upload_files")
    return files   

@file_router.post("/upload/bylink")
async def upload_video_by_link(links: list[str]):
    files = await upload_files_link(links, "/Users/kekehaha/python/detection/video2photo/582858358/videos/link")
    return files