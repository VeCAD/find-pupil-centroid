import cv2

class PreProcess():
    """
    Preprocessing on the incoming color image
    and that includes morphological filtering
    """
    def __init__(self, threshold = 70):
        self.threshold = threshold

    def __del__(self):
        pass

    def pre_processing(self, frame):
        # Convert rgb image to greyscale
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Threshold to get ROI - black/0
        _, thresh_img = cv2.threshold(grey, self.threshold , 255, cv2.THRESH_BINARY)

        # Erode reconstruct ROI area in case of ROI area
        # reduction after threshold due to lighting/reflection
        thresh_img = cv2.erode(thresh_img, None, iterations=6)

        # Reduce noisy areas around ROI
        thresh_img = cv2.dilate(thresh_img, None, iterations=4)
        thresh_img = cv2.medianBlur(thresh_img, 5)
        return thresh_img
