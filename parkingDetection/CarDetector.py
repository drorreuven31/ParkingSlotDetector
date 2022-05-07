import cv2
import pickle
import numpy as np


def cropToPoly(img,pts):
    ## (1) Crop the bounding rect
    rect = cv2.boundingRect(pts)
    x, y, w, h = rect
    croped = img[y:y + h, x:x + w].copy()

    ## (2) make mask
    pts = pts - pts.min(axis=0)

    mask = np.zeros(croped.shape[:2], np.uint8)
    cv2.drawContours(mask, [pts], -1, (255, 255, 255), -1, cv2.LINE_AA)

    ## (3) do bit-op
    dst = cv2.bitwise_and(croped, croped, mask=mask)

    ## (4) add the white background
    bg = np.ones_like(croped, np.uint8) * 255
    cv2.bitwise_not(bg, bg, mask=mask)
    dst2 = bg + dst

    return dst

class CarDetector:
    def __init__(self,pos_file_path):
        pos_json = open(pos_file_path,'rb')
        self.parkingCords = pickle.load(pos_json)

    def is_parking_free(self,snapshot):

        for i,cords in enumerate(self.parkingCords):
                #cv2.polylines(snapshot,[cords],True,(255,0,0),2)

                imgGray = cv2.cvtColor(snapshot, cv2.COLOR_BGR2GRAY)
                imgBlur = cv2.GaussianBlur(imgGray,(3,3),1)
                imgThreshold = cv2.adaptiveThreshold(imgBlur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                     cv2.THRESH_BINARY_INV, 25, 16)
                crop = cropToPoly(imgThreshold, cords)
                img_crop = cropToPoly(snapshot, cords)
                imgMedian = cv2.medianBlur(crop,5)
                kernel = np.ones((3,3),np.uint8)
                imgDilate = cv2.dilate(crop,kernel,iterations=1)
                count = cv2.countNonZero(imgDilate)
                cv2.imshow("tresh"+str(i)+": "+str(count),imgDilate)
                cv2.imshow("img",img_crop)

                cv2.waitKey(5000)
                cv2.destroyAllWindows()

                if(count<2000):
                    return True

        return False



