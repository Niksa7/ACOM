import cv2

def RGB_Color(pixel): # Так как BGR
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    if r > g and r > b:
        return (0, 0, 255)
    elif g > r and g > b:
        return (0, 255, 0)
    else:
        return (255, 0, 0)

def Task8():
    video = cv2.VideoCapture(0)
    cv2.namedWindow("Red Cross", cv2.WINDOW_NORMAL)

    width = 640
    height = 480
    centerX = width // 2
    centerY = height // 2

    cv2.resizeWindow("Red Cross", width, height)

    while(True):
        ret, frame = video.read() # ret: это логическое значение (True или False), которое указывает, было ли успешно считано изображение с камеры.

        central_pixel = frame[centerY][centerX]

        color = RGB_Color(central_pixel)

        # Крест
        cv2.rectangle(frame, (300, 120), (340, 360), color, -1)
        cv2.rectangle(frame, (200, 220), (440, 260), color, -1)

        cv2.imshow("Red Cross", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    video.release()
    cv2.destroyAllWindows()

Task8()