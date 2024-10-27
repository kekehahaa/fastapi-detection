import yt_dlp, os, asyncio

from concurrent.futures import ThreadPoolExecutor

def download_video_sync(url: str, output_path : str, quality: str='bestvideo[ext=mp4]'):
    '''
        Dowload youtube video by link
        
        Parameters
        ----------
        url: str
            Url youtube video
        output_path : str
            Path to directory where saving videos
        quality : str
            Quality of downloading video. The default is bestvideo[ext=mp4]
        '''
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    ydl_opts = {
        'format': quality,
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'prefer_ffmpeg': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_file = ydl.prepare_filename(info_dict)
        return video_file
    
async def donwload_video_async(url, output_path : str, quality: str='bestvideo[ext=mp4]'):
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        video_file = await loop.run_in_executor(pool, download_video_sync, url, output_path, quality)
    return video_file
    
def get_video_info(url):
    video_info = yt_dlp.YoutubeDL().extract_info(url=url, download=False)
    return video_info
    
if __name__ == "__main__":
    print(download_video_sync("https://www.youtube.com/watch?v=njX2bu-_Vw4", "/Users/kekehaha/python/detection/video2photo/582858358/videos"))