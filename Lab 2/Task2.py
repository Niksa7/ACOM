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
    create_window("Object Tracking", 0, 0)
    create_window("Threshold", 640, 0)

    if not cap.isOpened():
        print("Невозможно открыть камеру.")
        exit()

    while(True):

        ret, frame = cap.read()
        # Изображение не получено - break
        if not ret:
            print("Невозможно получить frame.")
            break

        # Перевод изображения в цветовое пространство HSV
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        red_color_low = (0, 100, 100)
        red_color_high = (20, 255, 255)
        # Пороговая обработка(threshold) изображения,т.е.конвертирование пикселей вне заданного диапазона в 0 и наоборот
        only_red_hsv = cv.inRange(hsv, red_color_low, red_color_high)

        # побитовая операция И кадров (Применение маски к кадру)
        # bitwise_red = cv.bitwise_and(frame, frame, mask=only_red_hsv)

        cv.imshow("Object Tracking", hsv)
        cv.imshow("Threshold", only_red_hsv)
        # cv.imshow("Only Red mask", bitwise_red)

        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()








Task1()