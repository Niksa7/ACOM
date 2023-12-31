import cv2

def Task6():
    video = cv2.VideoCapture(0)
    color = (0, 0, 255)
    cv2.namedWindow("Red Cross", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Red Cross", 640, 480)
    while(True):
        ret, frame = video.read() # ret: это логическое значение (True или False), которое указывает, было ли успешно считано изображение с камеры.

        # Красный крест
        cv2.rectangle(frame, (300, 120), (340, 360), color, 2)
        cv2.rectangle(frame, (200, 220), (440, 260), color, 2)

        # Размытие
        #  ksize - размер ядра по Гауссу(нечеткие значения) ,SigmaX - стандартное отклонение ядра вдоль оси x
        frame[220:260, 200:440] = cv2.GaussianBlur(frame[220:260, 200:440], (15, 15), 0)

        cv2.imshow("Red Cross", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    video.release()
    cv2.destroyAllWindows()

Task6()