import numpy as np
import cv2

# 수평 위치, 수직 위치
def bit_op(x, y):
    img1 = cv2.imread("./test.jpg")
    img2 = cv2.imread("./opencv.png")

    h, w, c = img2.shape

    # 로고를 추가할 이미지 영역 지정
    roi = img1[y:h + y, x: w + x]

    # img2를 흑백이미지로 변환
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # 마스크 생성
    # 작업 이미지, 임계값, 최대값, 타입
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)

    # 반전 마스크 생성 (NOT 연산)
    mask_inv = cv2.bitwise_not(mask)

    # roi에서 로고에 해당하는 부분만 검정색으로 변경
    # bitwise_and 연산은 0이 아닌 부분만 연산
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    cv2.imshow("img1_bg", np.hstack((img1_bg, cv2.cvtColor(mask_inv, cv2.COLOR_GRAY2BGR))))

    # 로고 이미지에서 로고 부분만 추출
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
    cv2.imshow("img2_fg", np.hstack((img2_fg, cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR))))

    # 지정 위치에 로고와 배경을 합친 이미지 더하기
    result = cv2.add(img1_bg, img2_fg)
    img1[y:h + y, x: w + x] = result
    cv2.imshow("add result", result)

    # 전체 합친 결과물 출력
    cv2.imshow("result", img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 로고 위치 (x, y)
bit_op(10, 10)
