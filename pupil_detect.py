import time
import cv2
import argparse
import numpy as np
from logic_modules.get_display_frame import InputStream
from logic_modules.get_display_frame import DisplayStream
from logic_modules.pre_processing import PreProcess
from logic_modules.blob_detection import BlobDetect
from logic_modules.labeler import Labeler

class PupilDetect():
    """
    Pupil detect and track class
    """
    def __init__(self, video_file):
        self.input_stream = InputStream(video_file)
        self.cv_display = DisplayStream()
        self.preprocess = PreProcess(threshold=70)
        self.detect_blob = BlobDetect()
        self.labeling = Labeler()
        self.pupil_detect_frame = 0
        self.fps = 0

    def __del__(self):
        del self.input_stream
        del self.cv_display
        del self.preprocess
        del self.detect_blob
        del self.labeling

    def track_frame(self):
        while True:
            # Start of frame process
            now = time.time()

            # Get the frame to be processed from video file
            frame = self.input_stream.get_frame()

            # Preprocessing
            threshold = self.preprocess.pre_processing(frame)

            # Blob (pupil) detection
            keypoints = self.detect_blob.detect(threshold)

            if keypoints:
                self.pupil_detect_frame += 1

            # Labeler
            bw_label_img, rgb_label_img= self.labeling.label_frames(frame, threshold, keypoints,
                                                                    self.pupil_detect_frame,
                                                                    self.input_stream.frame_count,
                                                                    self.fps)
            # Display
            self.cv_display.add_frame(bw_label_img, "Prepocess and Blob Detection Output")
            self.cv_display.add_frame(rgb_label_img, "RGB Output with Pupil Region and Centroid ")

            # End of frame process
            end = time.time()
            self.fps = 1/(end-now)

def main():
    """
    Place videos in test_videos folder
    Usage python3 pupil_detect.py --video_file "/test_videos/filename.mkv"
    Default video python3 pupil_detect.py
    """
    try:
        default_video = "/pupil_detect/test_videos/sample.mkv"
        parser = argparse.ArgumentParser()
        parser.add_argument('--video_file', nargs='?', const=1, type=str, default=default_video)
        args = parser.parse_args()

        # Run pupil tracking
        track_pupil = PupilDetect(args.video_file)
        track_pupil.track_frame()

    except Exception as e:
        print("Error encountered ", e)

if __name__ == '__main__':
    main()
