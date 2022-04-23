import cv2
from threading import Thread

class Webcam:

    def __init__(self,url_rtsp):
        # using video stream from IP Webcam for Android

        self.video_capture = cv2.VideoCapture(url_rtsp)
        self.current_frame = self.video_capture.read()[1]

    # create thread for capturing images
    def start(self):
        Thread(target=self._update_frame, args=()).start()

    def _update_frame(self):
        while (True):
            try:
                self.current_frame = self.video_capture.read()[1]
            except:
                pass

    # get the current frame
    def get_current_frame(self):
        return self.current_frame