import numpy as np
import cv2

# 이미지를 흑백으로 로드
img = cv2.imread("./test.jpg", cv2.IMREAD_GRAYSCALE)

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# GrayScale 이미지, 적용될 최대값, 사용할 Adaptive Thresholding 알고리즘, 블럭 크기, 보정상수
# cv2.ADAPTIVE_THRESH_MEAN_C: 적용될 픽셀을 중심으로 block 크기의 영역의 픽셀값 평균 - 보정상수
# cv2.ADAPTIVE_THRESH_GAUSSIAN_C: 적용될 픽셀을 중심으로 block 크기 안에 있는 가우시안 윈도우 기반 가중치들의 합 - 보정상수
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 3)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 3)

cv2.imshow("origin", img)
cv2.imshow("cv2.THRESH_BINARY", th1)
cv2.imshow("cv2.ADAPTIVE_THRESH_MEAN_C", th2)
cv2.imshow("cv2.ADAPTIVE_THRESH_GAUSSIAN_C", th3)

cv2.waitKey(0)
cv2.destroyAllWindows()
