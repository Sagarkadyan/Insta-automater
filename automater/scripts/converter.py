import os
import subprocess

def convert_video(input_path, output_path):
    if os.path.exists(output_path):
        print(f"[⏭] Already converted: {output_path}")
        return
    print(f"[🎬] Converting {input_path} via FFmpeg...")
    subprocess.run([
        "ffmpeg", "-i", input_path,
        "-vf", "scale=720:1280,fps=30",
        "-c:v", "libx264", "-preset", "fast",
        "-c:a", "aac", "-b:a", "128k", output_path
    ])

