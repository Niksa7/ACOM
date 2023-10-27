import cv2 as cv
import numpy as np

# Функция Гаусса
def gauss(x, y, a, b, sigma):
    return (1 / (np.pi * (2 * sigma ** 2))) * np.exp(-((x-a) ** 2 + (y-b) ** 2) / (2 * sigma ** 2))

# Нормализированная матрица Гаусса
def gaussian_matrix(size, sigma):
    sum = 0
    # Исходная матрица
    matrix = np.ones((size, size))
    for i in range(size):
        for j in range(size):
            matrix[i, j] = gauss(i, j, (size - 1) // 2, (size - 1) // 2, sigma)
    # Нормализация
    for i in range(size):
        for j in range(size):
            sum += matrix[i, j]
    for i in range(size):
        for j in range(size):
            matrix[i, j] /= sum
    return matrix

# Реализация фильтра Гаусса
def my_gaussian_blur(img, size, sigma):
    # Так как Гауссовским ядром мы не можем доработать границы, то просто нарастим их и удалим после обработки
    border = size // 2
    Blur_img = cv.copyMakeBorder(img, border, border, border, border, cv.BORDER_REFLECT)
    # Вычислим Гауссовское ядро
    kernel = gaussian_matrix(size, sigma)
    # Применение операции свертки к изображению
    Blur_img = convolution(Blur_img, kernel)
    Blur_img_cropped = Blur_img[border:-border, border:-border]
    return Blur_img_cropped

# Свертка
def convolution(img, kernel):
    # Копируем изображение
    Blur_copy = img.copy()
    ksize = len(kernel)
    x0 = ksize // 2
    y0 = ksize // 2
    # Итерации по внутренним пикселям изображения
    for i in range(x0, Blur_copy.shape[0] - x0):
        for j in range(y0, Blur_copy.shape[1] - y0):
            val = 0
            for m in range(-(ksize // 2), ksize // 2 + 1):
                for n in range(-(ksize // 2), ksize // 2 + 1):
                    val += img[i + m, j + n] * kernel[m + (ksize // 2), n + (ksize // 2)]
            Blur_copy[i, j] = val
    return Blur_copy



def task1():

    img = cv.imread("pic1.png", cv.IMREAD_GRAYSCALE)

    sigma = 2.0
    ksize = 15
    # Blur_img = my_gaussian_blur(img, ksize, sigma)
    # cv.imshow(f'Blur_img ksize = {ksize} sigma = {sigma}', Blur_img)

    # Задание 4. Доп примеры
    Blur_img1 = my_gaussian_blur(img,7, 7)
    cv.imshow('Blur_img ksize = 31 sigma = 7', Blur_img1)
    #
    # Blur_img2 = my_gaussian_blur(img, 11, 15)
    # cv.imshow('Blur_img ksize = 11 sigma = 15', Blur_img2)


    # Задание 5 Реализация встроенным методом OpenCV
    imgBlur_CV2 = cv.GaussianBlur(img, (ksize, ksize), sigma)
    cv.imshow('Blur CV2', imgBlur_CV2)
    cv.waitKey(0)

task1()