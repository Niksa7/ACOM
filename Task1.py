import cv2

def Task1():
    img = cv2.imread(r'D:\cat.jpg')
    cv2.namedWindow("Image", cv2.WINDOW_FREERATIO)
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
Task1()