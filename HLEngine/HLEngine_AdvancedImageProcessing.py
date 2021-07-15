#author:Akhil P Jacob
#HLDynamic-Integrations
import os
import cv2
import numpy as np
from PIL import Image
recognizer=cv2.face.LBPHFaceRecognizer_create()
path='dataset'

def collectDataSet(filterName,Cam,TargetID):
    faceDetect = cv2.CascadeClassifier(filterName)
    cam = cv2.VideoCapture(Cam)
    id =TargetID
    sampleNum = 0
    while (True):
        ret, img = cam.read();
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.3, 5);
        for (x, y, w, h) in faces:
            sampleNum += 1
            print(sampleNum)
            cv2.imwrite("dataset/pythface." + str(id) + "." + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.waitKey(100)
        cv2.imshow('Dataset', img)
        cv2.waitKey(1)
        if (sampleNum > 100):
            break
    cam.release()
    cv2.destroyAllWindows()


def trainDataSet():
    def getImageWithID(path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faces = []
        IDs = []
        for imagePath in imagePaths:
            faceImg = Image.open(imagePath).convert('L')
            faceNp = np.array(faceImg, 'uint8')
            ID = int(os.path.split(imagePath)[-1].split('.')[1])
            faces.append(faceNp)
            IDs.append(ID)
            cv2.imshow('training', faceNp)
            cv2.waitKey(10)
        return np.array(IDs), faces

    Ids, faces = getImageWithID(path)
    recognizer.train(faces, np.array(Ids))
    recognizer.save('recognizer/trainingdata.yml')
    cv2.destroyAllWindows()


def lockTarget_IP(filterName,ip,user1,user2,user3,user4,user5,user6,user7,user8,user9,user10):
    faceDetect = cv2.CascadeClassifier(filterName)
    #camera="http://192.168.1.202:8080/video"
    cam = cv2.VideoCapture(ip)
    rec = cv2.face.LBPHFaceRecognizer_create();
    rec.read('recognizer/trainingdata.yml')
    # id=0
    # font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4)
    font = cv2.FONT_HERSHEY_SIMPLEX
    while (True):
        ret, img = cam.read();
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.3, 5);
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id, conf = rec.predict(gray[y:y + h, x:x + w])
            # if(<50):
            if (id == 1):
                id = user1
            elif (id == 2):
                id = user2
            elif (id == 3):
                id = user3
            elif (id == 4):
                id = user4
            elif (id == 5):
                id = user5
            elif (id == 6):
                id = user6
            elif (id == 7):
                id = user7
            elif (id == 8):
                id = user8
            elif (id == 9):
                id = user9
            elif (id == 10):
                id = user10

            else:
                id = 'unknown'
            # cv2.cv.putText(cv2.cv.fromarray(img),str(id),(x,y+h),font,255)
            cv2.putText(img, str(id), (x, y + h), font, 2, (255, 0, 0), 3);
        cv2.imshow('MATTBot 2020 Tracker', img)
        if (cv2.waitKey(1) == ord('q')):
            break;
    cam.release()
    cv2.destroyAllWindows()



def lockTarget_Camera(filterName,camera,user1,user2,user3,user4,user5,user6,user7,user8,user9,user10):
    faceDetect = cv2.CascadeClassifier(filterName)    
    cam = cv2.VideoCapture(camera)
    rec = cv2.face.LBPHFaceRecognizer_create();
    rec.read('recognizer/trainingdata.yml')
    # id=0
    # font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4)
    font = cv2.FONT_HERSHEY_SIMPLEX
    while (True):
        ret, img = cam.read();
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray, 1.3, 5);
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            id, conf = rec.predict(gray[y:y + h, x:x + w])
            # if(<50):
            if (id == 1):
                id = user1
            elif (id == 2):
                id = user2
            elif (id == 3):
                id = user3
            elif (id == 4):
                id = user4
            elif (id == 5):
                id = user5
            elif (id == 6):
                id = user6
            elif (id == 7):
                id = user7
            elif (id == 8):
                id = user8
            elif (id == 9):
                id = user9
            elif (id == 10):
                id = user10

            else:
                id = 'unknown'
            # cv2.cv.putText(cv2.cv.fromarray(img),str(id),(x,y+h),font,255)
            cv2.putText(img, str(id), (x, y + h), font, 2, (255, 0, 0), 3);
        cv2.imshow('MATTBot 2020 Tracker', img)
        if (cv2.waitKey(1) == ord('q')):
            break;
    cam.release()
    cv2.destroyAllWindows()





