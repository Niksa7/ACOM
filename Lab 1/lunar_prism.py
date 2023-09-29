import cv2

def Task6():
    video = cv2.VideoCapture(0)
    color = (2, 233, 252)
    cv2.namedWindow("Lunar prism", cv2.WINDOW_NORMAL)
    width = 640
    height = 480
    cv2.resizeWindow("Lunar prism", width, height)
    while(True):
        ret, frame = video.read() # ret: это логическое значение (True или False), которое указывает, было ли успешно считано изображение с камеры.

        # Красный крест
        cv2.circle(frame, (width // 2, height // 2 - 25), 75, color, 2)
        cv2.circle(frame, (width // 2, height // 2), 100, color, 2)

        cv2.imshow("Lunar prism", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    video.release()
    cv2.destroyAllWindows()

Task6()