import numpy as np
import cv2

img = cv2.imread("./test.jpg")

B = img.item(340, 200, 0)
G = img.item(240, 200, 1)
R = img.item(240, 200, 2)

print("before:", [B, G, R])

# 지정한 위치의 픽셀값을 0으로 지정 (B)
img.itemset((240, 200, 0), 0)

B = img.item(240, 200, 0)
print("after:", [B, G, R])