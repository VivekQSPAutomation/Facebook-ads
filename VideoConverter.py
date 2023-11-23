import os

from moviepy.editor import VideoFileClip

# Replace with your video file path
video_path = f"{os.getcwd()}/blank.mp4"

# Load the video
clip = VideoFileClip(video_path)

# Get the dimensions of the video
width, height = clip.size

# Calculate the dimensions for a 1:1 aspect ratio
new_width = min(width, height)
new_height = new_width

# Crop the video to the desired dimensions
clip = clip.crop(x1=(width - new_width) // 2, x2=width - (width - new_width) // 2,
                 y1=(height - new_height) // 2, y2=height - (height - new_height) // 2)

# Export the video with the new aspect ratio
output_path = "output_file.mp4"
clip.write_videofile(output_path, codec="libx264")

# Clean up temporary files
clip.close()


print(f"Video with 1:1 aspect ratio saved at: {output_path}")
