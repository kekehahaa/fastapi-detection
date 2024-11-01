from fastapi import APIRouter, UploadFile, Depends, File
from sqlalchemy.ext.asyncio import AsyncSession

from app.utils.files import upload_video_local, upload_video_link, cutting_into_frames
from app.core.config import settings
from app.db.database import get_async_session


import app.utils.videocutter as vdc


file_router = APIRouter(prefix='/video')

@file_router.post("/upload/local")
async def proccess_upload_video_local(video_file: UploadFile, session: AsyncSession = Depends(get_async_session)):
    file = await upload_video_local(video_file, settings.DB_PATH, session)
    return file

@file_router.get("/upload/link")
async def upload_video_by_link(link: str, session: AsyncSession = Depends(get_async_session)):
    file = await upload_video_link(link, settings.DB_PATH, session)
    return file

# @file_router.get("/cutter/frames")
# async def proccess_video_to_frames(path: str, fps: float = 1.5, save_pattern: str = f'frame_%04d.jpg'):
#     file = await cutting_into_frames(path, fps, save_pattern)
#     return file
