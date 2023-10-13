import cv2 as cv
import numpy as np

def gauss(x, y, a, b, sigma):
    part1 = 1 / (np.pi * (2 * sigma ** 2))
    part2 = np.exp(-((x-a) ** 2 + (y-b) ** 2) / (2 * sigma ** 2))
    return part1 * part2

def GGaussianBlur(img, kernel, sigma):


def Task1():

    img = cv.imread("pic1.png", cv.IMREAD_GRAYSCALE)

    sigma = 11
    kernel = 21
    # GausBlur = MyGaussianBlur(img, kernel, sigma)
    # cv.imshow(str(kernel) + 'x' + str(kernel) + ' and deviation ' + str(sigma), GausBlur)

    # Задание 5 Реализация встроенным методом OpenCV
    imgBlur_CV2 = cv.GaussianBlur(img, (kernel, kernel), sigma)
    cv.imshow('Blur_by_CV2', imgBlur_CV2)
    cv.waitKey(0)









Task1()