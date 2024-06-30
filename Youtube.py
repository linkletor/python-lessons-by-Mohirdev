from pytube import YouTube
import tkinter as tk 
from tkinter import filedialog

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Download completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

url = "https://www.youtube.com/watch?v=zhjYbGcByaY"
save_path = r"D:\Mohirdev Python Course"

download_video(url, save_path)
