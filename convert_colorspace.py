import numpy as np
import cv2

def hsv():
    blue = np.uint8([[[255, 0, 0]]])
    green = np.uint8([[[0, 255, 0]]])
    red = np.uint8([[[0, 0, 255]]])

    hsv_b = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
    hsv_g = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
    hsv_r = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)

    print(hsv_b, hsv_g, hsv_r)

hsv()