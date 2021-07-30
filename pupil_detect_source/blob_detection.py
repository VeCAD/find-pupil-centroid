import cv2
import numpy as np

class BlobDetect():
    """
    Detect blobs from the incoming threshold image
    """
    def __init__(self):
        # Define blob detection params
        # Googled some of it
        # tweaked to get the pupil region only
        # Also dependant on filtering params
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
        self.detector = cv2.SimpleBlobDetector_create(self.params)

    def __del__(self):
        pass

    def detect(self, frame):
        """
        Detect blobs based on parameters defined
        and return the keypoints
        """
        keypoints = self.detector.detect(frame)
        return keypoints
