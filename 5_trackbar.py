import numpy as np
import cv2

# 이벤트 감지 함수
def onChange(x):
    print("Change:", x)

def trackbar():
    # 이미지 배열 생성
    # 512 * 200 크기의 RGB
    img = np.zeros((200, 512, 3), np.uint8)
    
    # 지정한 이름의 윈도우 생성
    cv2.namedWindow("trackbar")

    # 트랙바 이름, 윈도우 이름, 현재 값, 최대, 변경 감지 함수
    cv2.createTrackbar("R", "trackbar", 0, 255, onChange)
    cv2.createTrackbar("G", "trackbar", 0, 255, onChange)
    cv2.createTrackbar("B", "trackbar", 0, 255, onChange)
    cv2.createTrackbar("0: OFF / 1: ON", "trackbar", 1, 1, onChange)

    while True:
        cv2.imshow("trackbar", img)
        k = cv2.waitKey(1) & 0xFF

        if k == 27:
            break

        # 트랙바 이름, 윈도우 이름
        r = cv2.getTrackbarPos("R", "trackbar")
        g = cv2.getTrackbarPos("G", "trackbar")
        b = cv2.getTrackbarPos("B", "trackbar")
        s = cv2.getTrackbarPos("0: OFF / 1: ON", "trackbar")

        if s == 0:
            img[:] = 0
        else:
            img[:] = [b, g, r]

    cv2.destroyAllWindows()

trackbar()
