import numpy as np
import cv2

def tracking(target):
    # 동영상 로드, 혹은 카메라 연결 가능
    cap = cv2.VideoCapture(target)

    while True:
        # 프레임 읽기
        ret, frame = cap.read()

        if not ret:
            print("프레임 읽기 실패")
            break

        # HSV 색공간으로 변환
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # HSV에서 BGR로 가정할 범위를 정의
        lower_blue = np.array([110, 50, 50])
        upper_blue = np.array([130, 255, 255])

        lower_green = np.array([50, 50, 50])
        upper_green = np.array([70, 255, 255])

        lower_red = np.array([-10, 50, 50])
        upper_red = np.array([10, 255, 255])

        # HSV 이미지에서 청색, 초록, 빨간색만 추출하기 위한 임계값
        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
        mask_green = cv2.inRange(hsv, lower_green, upper_green)
        mask_red = cv2.inRange(hsv, lower_red, upper_red)

        res1 = cv2.bitwise_and(frame, frame, mask=mask_blue)
        res2 = cv2.bitwise_and(frame, frame, mask=mask_green)
        res3 = cv2.bitwise_and(frame, frame, mask=mask_red)

        cv2.imshow("origin", frame)
        cv2.imshow("b", res1)
        cv2.imshow("g", res2)
        cv2.imshow("r", res3)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()


cam = input("외부 카메라 장비를 사용하시나요? y/n: ").lower()
if cam == "y":
    cam_num = int(input("장비 번호를 입력해주세요: "))
    tracking(cam_num)
else:
    print("샘플 비디오로 예제를 시작합니다")
    tracking("./test.mp4")


