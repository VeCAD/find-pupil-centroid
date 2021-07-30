DOCUMENTATION
=============
# 1. Contents:
```
.
├── /test_videos
├── /sample_output_img
├── /pupil_detect_source
├── docker-compose.yml
├── Dockerfile
├── run.sh
├── get_videos.sh
├── requirements.txt
├── README.md
```

# 2. Setup Guide

Install [Docker](https://docs.docker.com/engine/install/ubuntu/) and [docker-compose](https://docs.docker.com/compose/install/) on a host Ubuntu system. Follow the post install step here [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
so that docker can be run without sudo.

Clone git
```sh
cd ~
git clone https://github.com/VeCAD/find-pupil-centroid.git
```

Run the `get_videos.sh` originally from repo [cv_find_pupil_centroid](https://github.com/lackdaz/cv_find_pupil_centroid) to download to sample video into test_videos folder.
```sh
cd ~/find-pupil-centroid
chmod +x get_videos.sh
./get_videos.sh
```

## How to build and run container
```sh
# Build the image
cd ~/find-pupil-centroid && docker-compose build

#Run the program
docker-compose run pupil --video_file "/test_videos/sample.mkv"

#OR
chmod +x run.sh
./run.sh
```

Run the following if CV window failes to display on host PC
```sh
No protocol specified
Unable to init server: Could not connect: Connection refused

(UI:142): Gtk-WARNING **: 10:03:12.231: cannot open display: :1

xhost +local:docker

#OR
chmod +x run.sh
./run.sh
```

# 3. Comments
1. The pupil centroid algorithm implemented is based on commonly used blob detection method using 
   existing image processing functions in OpenCV:
   * pupil_detect.py - main function
   * pre_processing.py converts the RGB image to grayscale, followed by binary threshold to assign 
     the region of interest as black and non interest as white. This image is then sent through a 
     morphological and median filter to reduce the noise blobs or shapes around the pupil.
   * blob_detection.py uses the pre-processed frame to single out the pupil based on the detector
     parameters which results in keypoints (approx pupil center and size)
   * labeler.py labels the image based on the keypoints and indicators given
   * get_display_frame.py - CV video capture and imshow
   
2. Total acurracy is assumed here as succesful pupil detected frames over total frames processed

3. FPS in pupil_detect.py is defined as inverse of end-end time taken to process a single frame (from capture to display)

4. sample_output_img folder contains sample images of the detector output

5. Might be beneficial to migrate critical threshold and blob detection parameters to cv trackbar so that parameters can 
   be changed on the fly to handle various test cases.
