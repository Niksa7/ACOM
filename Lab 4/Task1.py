import cv2 as cv
import numpy as np

def canny(path, ksize, sigma):

    # 1 TASK - гауссовское размытие бинарного изображения
    gray_image = cv.imread(path, cv.IMREAD_GRAYSCALE)

    cv.imshow('Gray Image', gray_image)

    gaus_blur_image = cv.GaussianBlur(gray_image, (ksize, ksize), sigma)

    cv.imshow('Gaussian Blur Image', gaus_blur_image)

    cv.waitKey(0)
    cv.destroyAllWindows()


canny('images/img.png', 5, 5)