import cv2 as cv
import numpy as np

def gauss(x, y, a, b, sigma):
    part1 = 1 / (np.pi * (2 * sigma ** 2))
    part2 = np.exp(-((x-a) ** 2 + (y-b) ** 2) / (2 * sigma ** 2))
    return part1 * part2

def task1():

    def gaussian_matrix(size, sigma):
        # Исходная матрица
        matrix = np.ones((size, size))
        for i in range(size):
            for j in range(size):
                matrix[i, j] = gauss(i, j, (size - 1) // 2, (size - 1) // 2, sigma)
        return matrix

    # Средне квадратичное отклонение
    sigma = 5
    # Итоговые матрицы
    print(f"Gaussian Kernel of size {3}x{3}:\n")
    kernel = gaussian_matrix(3, sigma)
    print(kernel)
    print("\n")
    print(f"Gaussian Kernel of size {5}x{5}:\n")
    kernel = gaussian_matrix(5, sigma)
    print(kernel)
    print("\n")
    print(f"Gaussian Kernel of size {7}x{7}:\n")
    kernel = gaussian_matrix(7, sigma)
    print(kernel)
    print("\n")

task1()