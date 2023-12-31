import cv2 as cv
import numpy as np

# Настройка окна
def create_window(name, x, y):
    cv.namedWindow(name, cv.WINDOW_NORMAL)
    cv.resizeWindow(name, 640, 480)
    cv.moveWindow(name, x, y)

def Task1():
    # Захват изображения с камеры
    cap = cv.VideoCapture(0)

    # Создание окна
    create_window("Normal", 0, 0)
    create_window("Object Tracking", 640, 0)

    if not cap.isOpened():
        print("Невозможно открыть камеру.")
        exit()

    while(True):

        ret, frame = cap.read()
        # Изображение не получено - break
        if not ret:
            print("Невозможно получить frame.")
            break

        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        cv.imshow("Normal", frame)
        cv.imshow("Object Tracking", hsv)

        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()


Task1()