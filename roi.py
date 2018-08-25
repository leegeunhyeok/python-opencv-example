# Region of image

import numpy as np
import cv2

img = cv2.imread("test.jpg")
cv2.imshow("original", img)

# (120, 150) ~ (180, 300) 위치의 픽셀 잘라내기 = 150 * 60 크기의 이미지
subimg = img[120:180, 150:300]
cv2.imshow("cutting", subimg)

# 원본 이미지의 (0, 0) ~ (60, 150) 위치에 자른 이미지 붙여넣기
img[0:60, 0:150] = subimg

# 이미지 크기 출력
print(img.shape)
print(subimg.shape)

# 수정된 이미지 출력
cv2.imshow("modified", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
