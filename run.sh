#!/bin/bash
xhost +local:docker &&
docker-compose run pupil --video_file "/test_videos/sample.mkv"
