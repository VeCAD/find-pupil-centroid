import sys
import time
import cv2

class InputStream():
    """
    Reads video file
    """
    def __init__(self, video_file):
        self.video_file = video_file
        self.cap = cv2.VideoCapture(self.video_file)
        self.width = self.cap.get(3)
        self.height = self.cap.get(4)
        self.fps = self.cap.get(5)
        self.frame_count = 0

    def __del__(self):
        self.cap.release()

    def get_frame(self):
        while True:
            if self.cap.isOpened():
                ret, frame = self.cap.read()
                if ret:
                    self.frame_count += 1
                    return frame
                else:
                    break

class DisplayStream():
    """
    Press Spacebar to pause/resume video
    and Q to quit while playing
    """
    def __init__(self):
        pass

    def __del__(self):
        cv2.destroyAllWindows()

    def add_frame(self, frame, window_name):
        key = cv2.waitKey(1)
        if key == 32:
            cv2.waitKey()
        elif key == ord('q'):
            sys.exit()

        cv2.imshow(window_name, frame)
