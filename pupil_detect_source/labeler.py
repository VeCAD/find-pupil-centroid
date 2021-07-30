import cv2
import numpy as np

class Labeler():
    """
    Gets keypoints and indicators and labels the image
    """
    def __init__(self):
        pass

    def __del__(self):
        pass

    def label_frames(self, frame, thresh_img, keypoints, pupil_detect_count, total_frame_count, fps):
        # Black and white image labelling
        # Threshold image with pupil area and centroid labeled
        bw_img = cv2.drawKeypoints(thresh_img, keypoints, np.array([]),(0, 0, 255),
                                   cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        for keyPoint in keypoints:
            center_x = keyPoint.pt[0]
            center_y = keyPoint.pt[1]
            cv2.drawMarker(bw_img, (int(center_x), int(center_y)), (0, 0, 255), markerType=cv2.MARKER_CROSS)

        # RGB image labelling
        # Acurracy is assumed here as succesful pupil detected frames over
        # total frames processed
        det_accu = pupil_detect_count/total_frame_count*100
        # Accuracy
        cv2.putText(frame, "Accuracy(%): {:.2f}".format(det_accu),
                    (int(20), int(40)), 0, 5e-3 * 200, (90, 255, 120), 2)
        # FPS
        cv2.putText(frame, "FPS: {:.2f}".format(fps),
                    (int(20), int(80)), 0, 5e-3 * 200, (40, 180, 200), 2)
        # Frame count
        cv2.putText(frame, "Frame count: {}".format(total_frame_count),
                    (int(20), int(120)), 0, 5e-3 * 200, (180, 255, 0), 2)
        # RGB frame with pupil area and centroid labeled
        frame = cv2.drawKeypoints(frame, keypoints, np.array([]), (90, 255, 120),
                                  cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        for keyPoint in keypoints:
            center_x = keyPoint.pt[0]
            center_y = keyPoint.pt[1]
            cv2.drawMarker(frame, (int(center_x), int(center_y)), (90, 255, 120), markerType=cv2.MARKER_CROSS, thickness=2)

        return bw_img, frame
