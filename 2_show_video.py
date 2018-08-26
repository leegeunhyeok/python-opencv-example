import cv2

def show_video(file_name):
    # 동영상 불러오기
    cap = cv2.VideoCapture(file_name)

    # 3: Width, 4: Height
    cap.set(3, 480)
    cap.set(4, 320)

    while True:
        # 프레임 1개씩 읽기
        # 정상적으로 읽었으면 ret = True
        ret, frame = cap.read()

        if not ret:
            print("비디오 읽기 오류")
            return

        # 색 변환
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # frame 그대로 출력할 경우 동영상 원본 재생
        # flip을 통해 이미지 뒤집기
        cv2.imshow("Video frame", cv2.flip(gray, 0))

        # ESC 누르면 종료
        k = cv2.waitKey(1)
        if k == 27:
            break
    
    # 열었던 Cap 객체를 해제
    cap.release()

    # 윈도우 모두 닫기
    cv2.destroyAllWindows()

show_video("./test.mp4")
