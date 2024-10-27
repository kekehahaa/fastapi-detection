from fastapi import HTTPException, UploadFile, status
from pathlib import Path

import app.utils.constants as cnst

def check_video_format(files: list[UploadFile]):
    for file in files:
        if Path(file.filename).suffix not in ('.mkv', '.mov', '.webm', '.mp4', '.avi', '.wmv'):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=cnst.BAD_VIDEO.format(file.filename))
        
def check_file_data(file: UploadFile):
    if file.size == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=cnst.NO_FILES)
    
def check_youtube_link(links: str):
    for link in links:
        if not link.startswith("https://www.youtube.com/watch?v"):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=cnst.BAD_LINK.format(link))
        
def check_not_null(links: str):
    if len(links) == 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=cnst.NULL)