import numpy as np
import cv2
from random import shuffle
import math

# 사각형/원 모드, 마우스클릭(그리기), 마우스클릭종료(그리기끝) 
mode, drawing = True, False

# 시작 x, y 위치
ix, iy = -1, -1

R = [i for i in range(256)]
G = [i for i in range(256)]
B = [i for i in range(256)]

def onMouse(event, x, y, flags, param):
    global ix, iy, drawing, mode, R, G, B

    if event == cv2.EVENT_LBUTTONDOWN:
        # 마우스 좌측버튼 클릭 시 그리기 시작
        drawing = True

        # 시작 위치 저장
        ix, iy = x, y

        # 색상 섞기
        shuffle(R), shuffle(G), shuffle(B)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            # 마우스가 움직일 경우 & 그리기 중
            if mode:
                # 모드에 따라 사각형/원 그리기
                cv2.rectangle(param, (ix, iy), (x, y), (R[0], G[0], B[0]), -1)

            else:
                r = (ix - x) ** 2 + (iy - y) ** 2
                r = int(math.sqrt(r))
                # 반지름
                cv2.circle(param, (ix, iy), r, (R[0],  G[0], B[0]), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        # 그리기 종료
        drawing = False

def mouseBrush():
    global mode

    img = np.zeros((512, 512, 3), np.uint8)
    cv2.namedWindow('paint2')
    cv2.setMouseCallback('paint2', onMouse, param=img)

    while True:
        cv2.imshow('paint2', img)
        k = cv2.waitKey(1) & 0xFF

        if k == 27:
            break
        elif k == ord('m'):
            # 'm' 키를 눌러 모드를 변경
            mode = not mode

    cv2.destroyAllWindows()

mouseBrush()
