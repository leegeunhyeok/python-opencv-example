import cv2

def show_image(file_name):
    # 이미지 파일 읽기
    img = cv2.imread(file_name, cv2.IMREAD_COLOR)
    
    # 윈도우 타이틀, 크기 지정
    cv2.namedWindow('Image show', cv2.WINDOW_AUTOSIZE)

    # 윈도우 타이틀
    cv2.imshow('Image show', img)

    # 키 입력 ms 만큼 대기, 0일 경우 계속 대기
    cv2.waitKey(0)

    # 윈도우 모두 닫기
    cv2.destroyAllWindows()

show_image("./test.jpg")
