import numpy as np
import cv2

# 이미지를 흑백으로 로드
img = cv2.imread("./test.jpg", cv2.IMREAD_GRAYSCALE)

# 이미지, 문턱값, 문턱값모다 클 경우 적용할 값, 옵션
# img, threshold_value, value,  flag
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) # 문턱 < 값 = value (반대: 0 으로 할당)
ret, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV) # 문턱 < 값 = 0 (반대: value 으로 할당)
ret, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC) # 문턱 < 값 = 문턱값 (반대: 원본유지)
ret, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO) # 문턱 < 값 = 원본유지 (반대: 0 으로 할당)
ret, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV) # 문턱 < 값 = 0 (반대: 원본유지)

# 이미지 출력
cv2.imshow("origin", img)
cv2.imshow("cv2.THRESH_BINARY", th1)
cv2.imshow("cv2.THRESH_BINARY_INV", th2)
cv2.imshow("cv2.THRESH_TRUNC", th3)
cv2.imshow("cv2.THRESH_TOZERO", th4)
cv2.imshow("cv2.THRESH_TOZERO_INV", th5)

cv2.waitKey(0)
cv2.destroyAllWindows()
