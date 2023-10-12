import cv2

def Task1():
    cap = cv2.VideoCapture(0)
    frames = 0
    cv2.namedWindow("Control", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Control", 640, 480)
    while(True):
        ret, frame = cap.read()

        if not (ret):
            print("Cannot open the web cam")
            return 0


        HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


        iLowH, iHighH, iLowS, iHighS, iLowV, iHighV = 170, 179, 150, 255, 60, 255



        iLastX = -1
        iLastY = -1

        cv2.imshow("Control", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
Task1()