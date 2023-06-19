import os
from converting import extract_frames


def main():

    video_path = "video/car_3.mov"
    output_folder = "output"
    include_parent = False
    image_format = "jpeg"

    extract_frames(video_path, output_folder, include_parent, image_format)

if __name__ == "__main__":
    main()