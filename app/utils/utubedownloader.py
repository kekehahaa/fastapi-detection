import yt_dlp, os

def download_video(url, output_path, quality='bestvideo'):
    ydl_opts = {
        'format': quality,
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'prefer_ffmpeg': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_file = ydl.prepare_filename(info_dict)
        return video_file
    
def get_video_info(url):
    video_info = yt_dlp.YoutubeDL().extract_info(url=url, download=False)
    return video_info
    
if __name__ == "__main__":
    print(download_video("https://www.youtube.com/watch?v=-sLTAIqGJX8", "o2photo/582858358/videos"))
