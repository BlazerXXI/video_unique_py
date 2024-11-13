import os
import sys
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def get_ffmpeg_path():
    if getattr(sys, 'frozen', False):
        # If the application is launched from .exe (files are packaged)
        return os.path.join(sys._MEIPASS, 'ffmpeg', 'bin', 'ffmpeg.exe')
    else:
        # If it is launched from a Python script (developmental environment)
        return os.path.join(os.path.dirname(__file__), 'ffmpeg', 'bin', 'ffmpeg.exe')

def process_command(input_file, output_file, ffmpeg_cmd):
    # Set the way to FFMPEG
    ffmpeg_path = get_ffmpeg_path()
    command = f"\"{ffmpeg_path}\" -i \"{input_file}\" {ffmpeg_cmd} \"{output_file}\""
    subprocess.run(command, shell=True, check=True)

def get_video_duration(input_file):
    """Gets the duration of the video using ffprobe."""
    ffprobe_path = os.path.join(os.path.dirname(__file__), 'ffmpeg', 'bin', 'ffprobe.exe')
    command = [
        ffprobe_path, 
        "-v", "error", 
        "-show_entries", "format=duration", 
        "-of", "default=noprint_wrappers=1:nokey=1", 
        input_file
    ]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return float(result.stdout.strip()) if result.returncode == 0 else None

def process_video(input_file, output_folder):
    """Launches the video uniquesization with the specified methods."""
    unique_videos(input_file, output_folder)
    messagebox.showinfo("Done", "The video is successfully uniqueized!")

def select_file():
    """Opens a file selection dialog."""
    file_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
    if file_path:
        input_file_var.set(file_path)

def select_folder():
    """Opens a dialog box for choosing a folder."""
    folder_path = filedialog.askdirectory()
    if folder_path:
        output_folder_var.set(folder_path)

def unique_videos(input_file, output_folder):
    """Creates unique versions of the video."""
    # We get the duration of the video
    duration = get_video_duration(input_file)
    if duration is None:
        messagebox.showerror("Error "," failed to get the duration of the video.")
        return

    # 1. Winking and pruning
    process_command(input_file, f"{output_folder}/unique_1.mp4", f"-vf \"hflip\" -t {duration - 2}")

    # 2. Grounding with the animation of the appearance
    process_command(input_file, f"{output_folder}/unique_2.mp4", "-vf \"boxblur=10:enable='between(t,0,2)\"")

    # 3. Visual noise and mirroring
    process_command(input_file, f"{output_folder}/unique_3.mp4", "-vf \"hflip, noise=alls=20\"")

    # 4. Template + mirroring + animation
    process_command(input_file, f"{output_folder}/unique_4.mp4", "-vf \"hflip, boxblur=10:enable='between(t,0,2)\"")

    # 5. Darming along the edges, pruning and mirroring
    process_command(input_file, f"{output_folder}/unique_5.mp4", f"-vf \"vignette=PI/4, hflip\" -t {duration - 2}")

# Setting up the interface
root = tk.Tk()
root.title("Video uniqueizer")
root.geometry("500x300")

input_file_var = tk.StringVar()
output_folder_var = tk.StringVar()

# File selection
tk.Label(root, text="Select a video for unique:").pack(pady=10)
tk.Entry(root, textvariable=input_file_var, width=60, state="readonly").pack(pady=5)
tk.Button(root, text="Выбрать видео", command=select_file).pack(pady=5)

# Selecting File folders
tk.Label(root, text="Select a folder to preserve unique videos:").pack(pady=10)
tk.Entry(root, textvariable=output_folder_var, width=60, state="readonly").pack(pady=5)
tk.Button(root, text="Select the folder", command=select_folder).pack(pady=5)

# Launch button
tk.Button(root, text="Run the uniqueization", command=lambda: process_video(input_file_var.get(), output_folder_var.get())).pack(pady=20)

# Launch of the interface
root.mainloop()
