import cv2 as cv
import numpy as np

def gauss(x, y, a, b, sigma):
    return (1 / (np.pi * (2 * sigma ** 2))) * np.exp(-((x-a) ** 2 + (y-b) ** 2) / (2 * sigma ** 2))

def task1():

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

    # Средне квадратичное отклонение
    sigma = 2
    # Итоговые матрицы
    print(f"Гауссовское ядро размерностью {3}x{3} и средним квадратичным отклонением {sigma}:\n")
    kernel = gaussian_matrix(3, sigma)
    print(kernel)
    print("\n")
    print(f"Гауссовское ядро размерностью {5}x{5} и средним квадратичным отклонением {sigma}:\n")
    kernel = gaussian_matrix(5, sigma)
    print(kernel)
    print("\n")
    print(f"Гауссовское ядро размерностью {7}x{7} и средним квадратичным отклонением {sigma}:\n")
    kernel = gaussian_matrix(7, sigma)
    print(kernel)
    print("\n")
    # Нормализация ядра свертки важна, чтобы после применения свертки яркость изображения в целом оставалась неизменной.
task1()