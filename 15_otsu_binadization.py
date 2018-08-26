# Otsu's Binarization
# 이전 예제의 Thresholding에선 지정한 값으로 문턱값을 사용함
# Otsu's Binarization은 이미지 히스토그램을 분석한 후 중간값을 threshold 값으로 취함

import numpy as np
import cv2
import matplotlib.pyplot as plt

def thresholding():
    img = cv2.imread("./test3.jpg", cv2.IMREAD_GRAYSCALE)

    # 전역 thresholding 적용
    ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    # Otsu's Binarization
    ret, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 가우시간 블러 적용 후 Otsu's Binarization
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    ret, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    titles = ["original", "hist", "G-Thresholding",
              "original", "hist", "Otsu Thresholding",
              "Gaussian-filtered", "hist", "Otsu Thresholding"]

    images = [img, 0, th1, img, 0, th2, blur, 0, th3]

    for i in range(3):
        # Thresholding 전 이미지
        plt.subplot(3, 3, i*3+1)
        plt.imshow(images[i*3], "gray")
        plt.title(titles[i*3])
        plt.xticks([])
        plt.yticks([])

        # 히스토그램
        plt.subplot(3, 3, i*3+2)
        plt.hist(images[i*3].ravel(), 256)
        plt.title(titles[i*3+1])
        plt.xticks([])
        plt.yticks([])

        # Thresholding 후 이미지
        plt.subplot(3, 3, i*3+3)
        plt.imshow(images[i*3+2], "gray")
        plt.title(titles[i*3+2])
        plt.xticks([])
        plt.yticks([])

    # 결과 출력
    plt.show()

thresholding()
