import ffmpeg, os, random, shutil, string

from typing import List, Tuple

class VideoCutter:
    '''
    Class video manupulations
    '''
    def __init__(self, file_path: str):
        self.file_path = file_path
        
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File {self.file_path} not found")
        
        self.file_info = self._get_video_info()
    
    def video_to_frames(self, output_path: str, fps: int | float=1.5, save_pattern: str=f'frame_%04d.jpg'):
        '''
        Make frames(photos) from video
        
        Parameters
        ----------
        output_path : str
            Path to directory where saving frames
        fps : Union[float, int]
            Frequancy. The default is 1.5
        save_pattern : str
            Pattern to save frames. The default is f'frame_%04d.jpg'
        '''
        if not os.path.exists(output_path):
            os.makedirs(output_path)
            
        try:
            (
            ffmpeg
            .input(self.file_path)
            .output(os.path.join(output_path, save_pattern), vf=f"fps={fps}")
            .run()
            )     
            print(f"Frames saved: {output_path}")
        except ffmpeg.Error as e:
            print(f"Error while cutting into frames: {e}")
            
    def video_cut(self, output_name: str, start: int | float, end: int | float):
        '''
        Cut video by interval from start to end
        
        Parameters
        ----------
        output_name : str
             Name to save new video
        start : Union[int, float]
            Start from sec to cutting
        end : Union[int, float]
            End sec to cutting
        '''
        try:
            (
            ffmpeg
            .input(self.file_path, ss=start, to=end)
            .output(output_name, codec="copy")
            .run(overwrite_output=True)
            )     
            print(f"Video saved: {output_name}")
        except ffmpeg.Error as e:
            print(f"Error while cutting video: {e}")
            
    def cut_by_duration(self, output_path: str, duration: int | float):
        '''
        Cut video by intervals
        
        Parameters
        ----------
        output_path : str
            Path to directory where saving videos
        duration : Union[int, float]
            Length to cut videos
        '''
        if not os.path.exists(output_path):
            os.makedirs(output_path)   
        
        count = int(float(self.file_info['format']['duration']) // duration)
        rndm = ''.join(random.choices(string.ascii_letters, k=7))
        _, extention = os.path.splitext(os.path.basename(self.file_path))
        
        if count <= 1:
            shutil.copy(self.file_path, output_path)
            return
                 
        for i in range(count):
            start = i * count
            end = start + duration
            self.video_cut(os.path.join(output_path, f"video_{rndm}_{i}{extention}"), start, end)
    
    def cut_by_parts(self, output_path: str, parts: int):
        '''
        Parameters
        ----------
        output_path : str
            Path to directory where saving videos
        parts : int
            This is the number of parts you need to divide the video into
        '''
        if not os.path.exists(output_path):
            os.makedirs(output_path)  
        
        rndm = ''.join(random.choices(string.ascii_letters, k=7))
        _, extention = os.path.splitext(os.path.basename(self.file_path))
        duration = float(self.file_info['format']['duration']) / parts
            
        for i in range(parts):
            start = i * duration
            end = start + duration
            self.video_cut(os.path.join(output_path, f"video_{rndm}_{i}{extention}"), start, end)
            
    def cut_by_timecodes(self, output_path, timecodes: List[Tuple[float]]):
        if not os.path.exists(output_path):
            os.makedirs(output_path)  
            
        rndm = ''.join(random.choices(string.ascii_letters, k=7))
        _, extention = os.path.splitext(os.path.basename(self.file_path))
        
        i = 0
        for start, end in timecodes:
            self.video_cut(os.path.join(output_path, f"video_{rndm}_{i}{extention}"), start, end)
            i += 1
        
    def _get_video_info(self):
        return ffmpeg.probe(self.file_path)
    
if __name__ == "__main__":
    file_path = "/Users/kekehaha/mirea/systeam admin/fdf/жесткий конфликт аункера с овердрайвом на медиа-лиге по контре 2 - это правда..mp4"
    out_path = "/Users/kekehaha/python/detection/video2photo/582858358/videos/bytimecodes"
    video = VideoCutter(file_path)
    video.video_to_frames("/Users/kekehaha/python/detection/video2photo/582858358/1", 2, f'video_%04d.jpg')
    # video.video_cut(out_path, 1, 6)
    # video.cut_by_duration(out_path, 1)
    # video.cut_by_parts(out_path, 15)
    video.cut_by_timecodes(out_path, [(11, 20)])
    
