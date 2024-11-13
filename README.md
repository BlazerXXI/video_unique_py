# Video Uniquizer

This project is a Python-based graphical application for creating unique versions of a video. The application uses `ffmpeg` to apply various effects to the video, such as mirroring, noise addition, and vignette effects, generating five different versions of the original video.

## Features

- Mirroring and video trimming
- Adding blur and animation effects
- Applying visual noise
- Vignetting around the edges
- Saving results in a specified output folder

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/video-uniquizer.git
    cd video-uniquizer
    ```

2. Ensure you have Python 3.7 or higher installed.

3. Install required dependencies:
    ```bash
    pip install tkinter
    ```

4. Download `ffmpeg` and add it to the project folder:
    - Create an `ffmpeg/bin` folder in the project root directory, then place `ffmpeg.exe` and `ffprobe.exe` in this folder.
    - Or install [FFmpeg](https://ffmpeg.org/download.html) and add it to your system `PATH`.

## Usage

1. Run the application:
    ```bash
    python video_uniquizer.py
    ```

2. In the graphical interface:
    - Click "Select Video" to choose the input video in MP4 format.
    - Click "Select Folder" to specify the output folder for the unique videos.
    - Click "Start Uniquization" to initiate the process.

3. The application will create five unique versions of the video in the specified folder, each with distinct effects for uniquization.

## Project Structure

- `video_uniquizer.py`: the main Python script containing the graphical interface and video uniquization logic.
- `ffmpeg/bin/ffmpeg.exe` and `ffmpeg/bin/ffprobe.exe`: `ffmpeg` and `ffprobe` executables for video processing.

## Error Handling

If an error occurs during video processing, the application will display an error message explaining the issue to help users troubleshoot.

## Example Output

After running the program, you will obtain five unique video files, each with different visual effects:

1. `unique_1.mp4`: mirrored and trimmed.
2. `unique_2.mp4`: initial blur effect.
3. `unique_3.mp4`: mirrored with added noise.
4. `unique_4.mp4`: combined blur and mirroring.
5. `unique_5.mp4`: vignetting effect and mirroring.

## Dependencies

- `ffmpeg` — for video processing and uniquization.
- `tkinter` — for creating the graphical interface.
