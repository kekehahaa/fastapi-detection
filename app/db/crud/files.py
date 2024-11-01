from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from app.db.models import Video


async def db_upload_video_file(name: str, path: str, video_size: int,
                               session: AsyncSession, link: str=None):
    new_video = Video(
        name=name,
        path=path,
        size=video_size,
        link=link
    )
    session.add(new_video)
    await session.commit()
    return new_video
