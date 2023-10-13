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
    create_window("Normal", 1280, 0)

    if not cap.isOpened():
        print("Невозможно открыть камеру.")
        exit()

    kernel = np.ones((5, 5), np.uint8)

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
        # Пороговая обработка изображения,т.е.конвертирование пикселей вне заданного диапазона в 0 и наоборот
        only_red_hsv = cv.inRange(hsv, red_color_low, red_color_high)

        # Морфологические операции
        # операция открытия - позволяет удалить шумы и мелкие объекты на изображении
        opening = cv.morphologyEx(only_red_hsv, cv.MORPH_OPEN, kernel)
        # операция закрытия - позволяет заполнить маленькие пробелы и разрывы в объектах на изображении
        closing = cv.morphologyEx(only_red_hsv, cv.MORPH_CLOSE, kernel)

        # # erode - сужение, эрозия, уменьшает размер объектов на черном фоне, для удаления мелких шумов
        # erode = cv.erode(only_red_hsv, kernel)
        # # dilate - расширение, увеличивает размер объектов, заполнение мелких дыр
        # dilate = cv.dilate(only_red_hsv, kernel)

        # побитовая операция И кадров (Применение маски к кадру)
        # bitwise_red = cv.bitwise_and(frame, frame, mask=only_red_hsv)

        # Нахождение моментов
        moments = cv.moments(closing)

        # Площадь, нулевой момент
        M01 = moments['m01']
        M10 = moments['m10']
        area = moments['m00']

        if area > 500:
            # Определение координат центров масс
            Cx = int(M10 / area)
            Cy = int(M01 / area)

            # Находим контуры
            contours, hierarchy = cv.findContours(closing, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

            max_cnt = max(contours, key=cv.contourArea)

            # Извлекаем характеристики прямоугольника, охватывающего контур
            x, y, w, h = cv.boundingRect(max_cnt)

            cv.rectangle(frame, (Cx - w//2, Cy - h//2), (Cx + w//2, Cy + h//2), (0, 0, 0), 2)

        # cv.imshow("Erode", erode)
        # cv.imshow("Dilate", dilate)
        # cv.imshow("Opening", opening)
        # cv.imshow("Closing", closing)
        cv.imshow("Object Tracking", hsv)
        cv.imshow("Threshold", only_red_hsv)
        cv.imshow("Normal", frame)
        # cv.imshow("Only Red mask", bitwise_red)

        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

Task1()