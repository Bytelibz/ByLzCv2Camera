#importing
import cv2
import requests
import numpy as np
import imutils
import os
#Here, instead of 'C:\opencv-4.x\data\haarcascades\haarcascade_frontalface_default.xml', insert 'your path\haarcascade_frontalface_default.xml'
haar_cascade = cv2.CascadeClassifier('C:\opencv-4.x\data\haarcascades\haarcascade_frontalface_default.xml')
url = "http://yourip//shot.jpg" #Using ipwebcam


Shable = 1 #instead true
#function of displaying constant camera viewing, with drawing of detected faces
def maincam():
    if Shable == 1:
        while True:
            img_resp = requests.get(url)
            img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
            img = cv2.imdecode(img_arr, -1)
            img = imutils.resize(img, width=1000, height=1800)
            fps = int(1)
            faces_rect = haar_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=9)
            for (x, y, w, h) in faces_rect:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), thickness=2)

            cv2.imshow("ByLz", img)
            isWritten = cv2.imwrite('detected.png', img)   
            if cv2.waitKey(1) == 27:
                break

        cv2.destroyAllWindows()
#face detection function without constantly viewing the camera
def maincamtrigger():
    if Shable == 1:
        while True:
            img_resp = requests.get(url)
            img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
            img = cv2.imdecode(img_arr, -1)
            img = imutils.resize(img, width=1000, height=1800)
            fps = int(1)
            faces_rect = haar_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=9)
            for (x, y, w, h) in faces_rect:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), thickness=2)
                print('Some face detected, do u need to show y/n')
                LastWritten = cv2.imwrite('C:\ByLz\data\images\lastdetected.png', img)
                
                sh1 = input()
                if sh1 == 'y':
                    img = mpimg.imread('C:\ByLz\data\images\lastdetected.png')
                    imgplot = plt.imshow(img)
                    plt.show()
                if sh1 == 'n':
                    os.system('cls')       

            
