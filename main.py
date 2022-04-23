import cv2
import matplotlib.pyplot as plt
import time
from Webcam import Webcam
from parkingDetection.CarDetector import CarDetector
from whatsappBot import send_message
# get image from webcam

def show_snap(cam):
    image = cam.get_current_frame()
    cv2.imshow('image',image)
    cv2.waitKey(1)

def main():
    url_rtsp = 'rtsp://dror:1234@192.168.1.30:8554/live'
    url_rtsp2 = 'rtsp://dror:1234@192.168.1.30:8080/h264_ulaw.sdp'
    #cam = Webcam(url_rtsp)
    #cam.start()
    car_detector = CarDetector('parkingDetection/pos.txt')


    img = cv2.imread('pic.jpg')

    cropped_image = img[422:422 + 600, 327:327 + 1000]

    #img = cv2.resize(cropped_image,(360,240))

    car_detector.is_parking_free(cropped_image)
    # while True:
    #     time.sleep(2)
    #     image = cam.get_current_frame()
    #     show_snap(cam)
    #     # if(car_detector.is_parking_free(image)):
    #     #     send_message ('parking is free')
    #     # else:
    #     #     send_message('parking is taken')

if __name__ == "__main__":
    main()