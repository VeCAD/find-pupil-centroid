DOCUMENTATION
=============
# 1. Contents:
```
.
├── /test_videos             - Test video folder
├── /sample_output_img       - Sample output images
├── /logic_modules           - Contains pupil detect logic py modules
├── docker-compose.yml       - compose yml 
├── Dockerfile               - Dockerfile 
├── run.sh                   - Run program script
├── get_videos.sh            - Get sample video script
├── requirements.txt         - pip3 install txt
├── README.md                - Guide to use this repo
├── pupil_detect.py          - Main function
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
docker-compose run pupil --video_file "/pupil_detect/test_videos/sample.mkv"

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

To run the program inside the Docker container terminal, comment out the following inside Dockerfile
```sh
#ENTRYPOINT ["python3", "pupil_detect.py"]
```
Then
```sh
docker-compose build
docker-compose run pupil bash
# in container terminal
python3 pupil_detect.py --video_file "/pupil_detect/test_videos/sample.mkv"
```

Playback controls 
```
Press Spacebar to pause CV display output
Press Q to quit anytime
```

# 3. Comments/Feedback
1. The pupil centroid algorithm implemented is based on commonly used blob detection method using 
   existing image processing functions in OpenCV:
   * pupil_detect.py - main function
   * pre_processing.py
       * converts the RGB image to grayscale
       * followed by binary threshold to assign the region of interest as black and non interest as white. 
       * the image is then sent through a morphological and median filter to reduce noisy blobs or shapes.
   * blob_detection.py uses the pre-processed frame to single out and track the pupil based on the detector
     parameters which results in pupil keypoints (approx pupil center and size)
   * labeler.py labels the image based on the keypoints and indicators given
   * get_display_frame.py - Displays the cv image frame given
   
2. Total acurracy is assumed here as succesful pupil detected frames over total frames processed.

3. FPS in pupil_detect.py is defined as inverse of end-end time taken to process a single frame (from capture to display)
   * Core i-7  80000 series Desktop CPU ~30fps
   * Jetson Nano ~7fps

4. sample_output_img folder contains sample images of the detector output

5. Might be beneficial to migrate critical threshold and blob detection parameters to cv trackbar so that parameters can 
   be tweaked on the fly to handle various test cases.
   ```py
   # in pre_processing.py
   _, thresh_img = cv2.threshold(grey, self.threshold , 255, cv2.THRESH_BINARY)
   ```

   ```py
   # in blob_detection.py
   self.params = cv2.SimpleBlobDetector_Params()
   self.params.blobColor = 0
   self.params.filterByArea = True
   self.params.minArea = 2000
   self.params.maxArea = 300000
   self.params.filterByCircularity = False
   self.params.filterByConvexity = True
   self.params.filterByInertia = True
   self.params.minInertiaRatio = 0.1
   self.params.maxInertiaRatio = 1
   ```

6. Time taken for assesment : ~6-7 hrs
