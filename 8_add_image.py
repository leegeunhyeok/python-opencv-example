import numpy as np
import cv2

def addImage(img1, img2):
    img1 = cv2.imread(img1)
    img2 = cv2.imread(img2)

    cv2.imshow("img1", img1)
    cv2.imshow("img2", img2)

    # Numpy 배열 더하기 (만약 더한 값이 255 범위를 벗어나면 값 % 256으로 변환)
    add_img1 = img1 + img2

    # opencv 더하기, 255를 넘을 경우 그냥 255로 지정
    add_img2 = cv2.add(img1, img2)

    cv2.imshow("img1 + img2", add_img1)
    cv2.imshow("cv2.add()", add_img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

addImage("./test.jpg", "./test2.jpg")
