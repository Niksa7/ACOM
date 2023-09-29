import cv2

url = 'http://192.168.0.200:8080/video'

def Task9():

    cap = cv2.VideoCapture(url)

    while True:

        ret, frame = cap.read()
        cv2.imshow('Phone Stream', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

Task9()