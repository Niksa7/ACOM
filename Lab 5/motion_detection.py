import cv2
import cv2 as cv

def motion_detection(src, output, ksize, sigma, porog, base_area):
    # Читаем видео из файла
    cap = cv.VideoCapture(src, cv.CAP_ANY)

    ret, frame = cap.read()
    if not cap.isOpened():
        print("Невозможно прочесть видео.")
        exit()

    # Бинаризация изображения
    gray_image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Гауссовское размытие
    gg_image = cv.GaussianBlur(gray_image, (ksize, ksize), sigma)
    # Кодек
    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    # Высота и ширина кадра для записи
    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

    video_writer = cv.VideoWriter('Output_videos/' + output + '.mp4', fourcc, 24, (width, height))

    while True:

        # Copy предыдущий кадр
        prev_image = gg_image.copy()

        # Новый кадр
        ret, next_frame = cap.read()
        
        # Eсли чтение неуспешно, остановить цикл
        if not ret:
            break

        gray_image = cv.cvtColor(next_frame, cv.COLOR_BGR2GRAY)
        gg_image = cv.GaussianBlur(gray_image, (ksize, ksize), sigma)

        # Вычисляет абсолютную разницу между двумя изображениями.
        frame_diff = cv.absdiff(gg_image, prev_image)

        # Применяет пороговое(бинарное) значение к изображению. Тип пороговой обработки
        porog, frame_treshold = cv.threshold(frame_diff, porog, 255, cv.THRESH_BINARY)

        # Поиск контуров. Режим поиска контура. Метод аппроксимации контура.
        contours, hierarchy = cv.findContours(frame_treshold, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            # Площадь контура
            area = cv.contourArea(contour)

            if area > base_area:
                video_writer.write(next_frame)

    video_writer.release()

# Размытие
ksize = 3
sigma = 50
# Обнаружение ложных срабатываний
porog = 60
base_area = 20
motion_detection('Videos/LR4_main_video.mov', 'output_video_1', ksize, sigma, porog, base_area)














