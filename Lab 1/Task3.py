import cv2
def Task3(path, scale_x, scale_y, color):
    cap = cv2.VideoCapture(path, cv2.CAP_ANY)

    while (True):
        ret, frame = cap.read()

        if not(ret):
            break

        frame = cv2.resize(frame, (0, 0), fx=scale_x, fy=scale_y)
        frame = cv2.cvtColor(frame, color)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

Task3('D:/sample-5s.mp4', 0.5, 0.5, cv2.COLOR_BGR2GRAY)
Task3('D:/cat.jpg', 1, 1, cv2.COLOR_BGR2RGB)
Task3('https://media.geeksforgeeks.org/wp-content/uploads/20210314115545/sample-video.mp4', 0.2, 0.2, cv2.COLOR_BGR2HSV)
