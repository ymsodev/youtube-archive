import tempfile

import yt_dlp
import openai

URLS = ['https://www.youtube.com/watch?v=tDexugp8EmM']

def download_youtube_video(output_path, urls):
    path = f'{output_path}/temp.%(ext)s'
    ydl_opts = {
        'format': 'mp3/bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }],
        'outtmpl': path,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(urls)

with tempfile.TemporaryDirectory() as tmpdirname:
    download_youtube_video(tmpdirname, URLS)
    with open(f"{tmpdirname}/temp.mp3", "rb") as f:
        transcript = openai.Audio.transcribe("whisper-1", f)

with open("test.txt", "w") as f:
    f.write(transcript["text"])
