from fastapi import HTTPException, UploadFile, status
from pathlib import Path

import app.utils.constants as cnst

def check_video_format(file: UploadFile):
    if Path(file.filename).suffix.lower() not in ('.mkv', '.mov', '.webm', '.mp4', '.avi', '.wmv'):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=cnst.BAD_VIDEO.format(file.filename))
        
def check_file_data(file: UploadFile):
    if file.size == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=cnst.NO_FILES)
    
def check_youtube_link(link: str):
    if not link.startswith("https://www.youtube.com/watch?v"):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=cnst.BAD_LINK.format(link))