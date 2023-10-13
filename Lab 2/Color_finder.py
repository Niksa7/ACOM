import cv2 as cv
import numpy as np


def nothing(x):
    pass


def create_window(name, x, y, width, height):
    cv.namedWindow(name, cv.WINDOW_NORMAL)
    cv.resizeWindow(name, width, height)
    cv.moveWindow(name, x, y)


def Task1():
    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        print("Невозможно открыть камеру.")
        exit()

    create_window("Original", 800, 150, 640, 480)
    create_window("Threshold", 1450, 150, 640, 480)
    create_window("setup", 0, 150, 640, 480)

    # Инициализация trackbars
    cv.createTrackbar("h1", "setup", 0, 180, nothing)
    cv.createTrackbar("s1", "setup", 0, 255, nothing)
    cv.createTrackbar("v1", "setup", 0, 255, nothing)
    cv.createTrackbar("h2", "setup", 180, 180, nothing)
    cv.createTrackbar("s2", "setup", 255, 255, nothing)
    cv.createTrackbar("v2", "setup", 255, 255, nothing)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Невозможно получить frame.")
            break

        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        # Получение значений из trackbars
        h1 = cv.getTrackbarPos('h1', 'setup')
        s1 = cv.getTrackbarPos('s1', 'setup')
        v1 = cv.getTrackbarPos('v1', 'setup')
        h2 = cv.getTrackbarPos('h2', 'setup')
        s2 = cv.getTrackbarPos('s2', 'setup')
        v2 = cv.getTrackbarPos('v2', 'setup')
        min_p = (h1, s1, v1)
        max_p = (h2, s2, v2)

        mask = cv.inRange(hsv, min_p, max_p)

        cv.imshow("Original", hsv)
        cv.imshow("Threshold", mask)

        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()


Task1()
