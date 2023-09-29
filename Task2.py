import cv2

def Task2(path, color, window_setting):
    img = cv2.imread(path, color)
    cv2.namedWindow("Cat", window_setting)
    img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    cv2.imshow("Cat", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

Task2('D:/cat.jpg', cv2.IMREAD_COLOR, cv2.WINDOW_FULLSCREEN)
Task2('D:/cat.jpg', cv2.IMREAD_GRAYSCALE, cv2.WINDOW_NORMAL)
Task2('D:/cat.jpg', cv2.IMREAD_REDUCED_COLOR_8, cv2.WINDOW_FREERATIO)