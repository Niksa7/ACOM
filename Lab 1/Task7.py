import cv2

def Task7():
    cap = cv2.VideoCapture(0)
    cv2.namedWindow("Video Recording", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Video Recording", 640, 480)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter("Task7_video.mp4", fourcc, 25, (640, 480))
    while(True):
        ret, frame = cap.read()
        cv2.imshow("Video Recording", frame)
        video_writer.write(frame)
        if cv2.waitKey(1) % 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()

Task7()