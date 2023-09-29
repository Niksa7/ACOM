import cv2

def Task5(path):
    frame = cv2.imread(path)
    cv2.namedWindow('HSV', cv2.WINDOW_FREERATIO)
    cv2.namedWindow('not HSV', cv2.WINDOW_FREERATIO)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('not HSV', frame)
    cv2.imshow('HSV', hsv)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

Task5('D:/cat.jpg')