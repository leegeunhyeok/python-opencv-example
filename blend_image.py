import numpy as np
import cv2

def onChange(x):
    print(x)

def blendImage(img1, img2):
    img1 = cv2.imread(img1)
    img2 = cv2.imread(img2)

    cv2.namedWindow("Image blend")

    # 0 ~ 100 트랙바 생성
    cv2.createTrackbar("Mixing", "Image blend", 0, 100, onChange)
    
    # 초기값 0으로 지정
    mix = 0

    while True:
        # 블렌드 효과 (두 이미지 페이드 인 / 페이드 아웃)
        # g(x) = (1 - a) * f1(x) + a * f2(x)
        # a (0 ~ 1)값이 증가하면 f1 함수의 효과가 작아지고 f2가 증가, 줄어들경우 그 반대
        img = cv2.addWeighted(img1, float(100 - mix) / 100, img2, float(mix) / 100, 0)
        cv2.imshow("Image blend", img)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

        mix = cv2.getTrackbarPos("Mixing", "Image blend")
    
    cv2.destroyAllWindows()


blendImage("./test.jpg", "./test2.jpg")
