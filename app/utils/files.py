import os, aiofiles

from fastapi import HTTPException, status, UploadFile
from yt_dlp.utils import DownloadError


import app.utils.constants as cnst
import app.api.validators  as val
from app.utils.utubedownloader import donwload_video_async

async def upload_files_user(files: list[UploadFile], path: str) -> list[dict]:
    val.check_file_data(files[0])  # check if file is uploaded
    val.check_video_format(files)  # check if file is video
    uploaded_files = []
    for file in files:
        try:
            content = file.file.read()
            full_path = os.path.join(path, file.filename)
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
        uploaded_files.append({'status': 'uploaded', 'file_size': os.stat(full_path).st_size, 'file_path': full_path})
    return uploaded_files

async def upload_files_link(links: list[str], path: str):
    val.check_not_null(links)
    val.check_youtube_link(links)
    for link in links:
        try:
            video_file = await donwload_video_async(link, path)
        except DownloadError:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=cnst.BAD_W_FILE.format(path)
            )
    return "ok"
        
        
        
    
    