import cv2
import numpy as np
import pickle
from Webcam import Webcam
url_rtsp = 'rtsp://dror:1234@192.168.1.16:8554/live'


cam = Webcam(url_rtsp)
img = cam.get_current_frame()

img = img[422:422 + 600, 327:327 + 1000]

parkingCords = []
parking_i =0

def mouseClick(events,x,y,flags,params):
    global  parking_i
    if(events==cv2.EVENT_LBUTTONDOWN):
        if len(parkingCords) == parking_i:
            parkingCords.append([])
        parkingCords[parking_i].append([x,y])
        print("point added to parking {0} ({1},{2})".format(parking_i,x,y))
    elif(events==cv2.EVENT_RBUTTONDOWN):
        r_x,r_y =parkingCords[parking_i].pop()
        print("point removed from parking {0} ({1},{2})".format(parking_i, r_x, r_y))

    elif(events==cv2.EVENT_MBUTTONDOWN):
        parking_i += 1

        print('select next parking')




cv2.imshow("img",img)
cv2.setMouseCallback("img",mouseClick)
cv2.waitKey(0)




if len(parkingCords)>0:
    npparkingCords = np.array(parkingCords, np.int32)
    with open("pos.txt",'wb') as f:
        pickle.dump(npparkingCords,f)
