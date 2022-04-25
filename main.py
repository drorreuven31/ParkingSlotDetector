import cv2
import time
from Webcam import Webcam
from parkingDetection.CarDetector import CarDetector
from TelegramBot.TelegramParkingBot import TelegramParkingBot

# get image from webcam

def show_snap(cam):
    image = cam.get_current_frame()
    cv2.imshow('image',image)
    cv2.waitKey(1)

def main():
    url_rtsp = 'rtsp://dror:1234@192.168.1.30:8554/live'
    url_rtsp2 = 'rtsp://dror:1234@192.168.1.30:8080/h264_ulaw.sdp'
    bot_api_key ='5238370658:AAGVxqZbzpi2GOUaHf1MUBI_Mtugt4pf_a0'
    group_id = -612719174

    #cam = Webcam(url_rtsp)
    cam=1
    #cam.start()
    bot = TelegramParkingBot(bot_api_key,cam,group_id)
    bot.start_bot()
    car_detector = CarDetector('parkingDetection/pos.txt')


    img = cv2.imread('pic.jpg')

    cropped_image = img[422:422 + 600, 327:327 + 1000]

    #img = cv2.resize(cropped_image,(360,240))

    car_detector.is_parking_free(cropped_image)
    is_free = False
    while True:
        time.sleep(2)
        image = cam.get_current_frame()
        cropped_image = img[422:422 + 600, 327:327 + 1000]
        show_snap(cropped_image)
        curr_is_free = car_detector.is_parking_free(cropped_image)
        if(curr_is_free!=is_free): # only if there was a change is the state of the parking
            msg = 'parking is {}free'.format('' if curr_is_free else 'not ')
            bot.send_photo(image, msg, group_id)


if __name__ == "__main__":
    main()