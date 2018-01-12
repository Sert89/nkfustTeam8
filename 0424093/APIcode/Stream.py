import time
import cv2
from FaceAPI import faceAPI
class stream():
    video_capture=cv2.VideoCapture(0)
    initInf = faceAPI()
    initInf.get_groupList()
    initInf.get_groupUser()
    while True:
        ret, frame = video_capture.read()
        if cv2.waitKey(1) & 0xFF == ord('i'):
            identifyClassConnect = faceAPI()
            identifyClassConnect.identify_user(frame)
        if cv2.waitKey(1) & 0xFF == ord('t'):
            facefeatureClassConnect = faceAPI()
            facefeatureClassConnect.face_feature_detect(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        cv2.imshow('Py-QT-Stream',frame)
    video_capture.release()
    cv2.destroyAllWindows()
