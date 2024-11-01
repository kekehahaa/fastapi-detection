import os, aiofiles

from fastapi import HTTPException, status, UploadFile
from yt_dlp.utils import DownloadError
from pathlib import Path
from sqlalchemy.ext.asyncio import AsyncSession


import app.utils.constants as cnst
import app.api.validators  as val
from app.utils.utubedownloader import donwload_video_async
from app.db.crud.files import db_upload_video_file

async def upload_video_local(file: UploadFile, path: str, session: AsyncSession):
    val.check_file_data(file)  # check if file is uploaded
    val.check_video_format(file)  # check if file is video
    try:
        full_path = Path(path) / Path(file.filename).stem
        full_path.mkdir()
    except FileExistsError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=cnst.BAD_W_FILE.format(path)
        )
    full_path = full_path / file.filename
    try:
        content = file.file.read()
        async with aiofiles.open(full_path, 'wb') as f:
            await f.write(content)
    except OSError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=cnst.BAD_W_FILE.format(path)
        )
    finally:
        await f.close()
        file.file.close()
    db_crud = await db_upload_video_file(file.filename, str(full_path), os.stat(full_path).st_size, session)  # add info to db
    uploaded_file = {'status': 'uploaded', 'file_size': os.stat(full_path).st_size, 'file_path': full_path}
    return db_crud
    
async def upload_video_link(link: str, path: str, session: AsyncSession):
    val.check_youtube_link(link)
    try:
        video_file = await donwload_video_async(link, path)
    except DownloadError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=cnst.BAD_W_FILE.format(path)
        )
    
    db_crud = await db_upload_video_file(Path(video_file).name, str(video_file), os.stat(video_file).st_size, session)
    uploaded_file = {'status': 'uploaded', 'file_size': os.stat(video_file).st_size, 'file_path': video_file}
    return db_crud
        
async def cutting_into_frames():
    pass
        
        
    
    