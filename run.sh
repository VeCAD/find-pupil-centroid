#!/bin/bash
xhost +local:docker &&
docker-compose run pupil --video_file "/pupil_detect/test_videos/sample.mkv"
