import cv2
import os
from keras.models import load_model
import numpy as np
from pygame import mixer
import time
def stop1():
    exit()
mixer.init()
sound = mixer.Sound('Audio/alarm.wav')

face = cv2.CascadeClassifier('Haar_Cascades\haarcascade_frontalface_default.xml')
leye = cv2.CascadeClassifier('Haar_Cascades\haarcascade_lefteye_2splits.xml')
reye = cv2.CascadeClassifier('Haar_Cascades\haarcascade_righteye_2splits.xml')
mouth = cv2.CascadeClassifier('Haar_Cascades\haarcascade_frontalface_default.xml')

lbl = ['yawn', 'no_yawn', 'Close', 'Open']

model = load_model('Models/drowsiness_new6_2.h5')
path = os.getcwd()
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
count = 0
score = 0
thicc = 2
IMG_SIZE = 145

rpred = np.array([])
lpred = np.array([])
mpred = np.array([])

while (True):
    ret, frame = cap.read()
    height, width = frame.shape[:2]
    
    if(ret == False):
        print('Can not access the camera feed. Please try again !!!!')
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face.detectMultiScale(gray, minNeighbors=5, scaleFactor=1.1, minSize=(25, 25))
    left_eye = leye.detectMultiScale(gray)
    right_eye = reye.detectMultiScale(gray)

    cv2.rectangle(frame, (0, height - 50), (200, height), (0, 0, 0), thickness=cv2.FILLED)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y + (int)(h / 2)), (x + w, y + h), (100, 100, 100), 1)

    for (x, y, w, h) in right_eye:
        r_eye = frame[y:y + h, x:x + w]
        count = count + 1
        # r_eye = cv2.cvtColor(r_eye,cv2.COLOR_BGR2GRAY)
        r_eye = r_eye / 255
        r_eye = cv2.resize(r_eye, (IMG_SIZE, IMG_SIZE))
        r_eye = r_eye.reshape(-1, IMG_SIZE, IMG_SIZE, 3)
        # r_eye = np.expand_dims(r_eye,axis=0)
        rpred = model.predict(r_eye)
        if (np.argmax(rpred) == 2):
            lbl = 'Open'
        if (np.argmax(rpred) == 3):
            lbl = 'Closed'
        break

    for (x, y, w, h) in left_eye:
        l_eye = frame[y:y + h, x:x + w]
        count = count + 1
        # l_eye = cv2.cvtColor(l_eye,cv2.COLOR_BGR2GRAY)
        l_eye = l_eye / 255
        l_eye = cv2.resize(l_eye, (IMG_SIZE, IMG_SIZE))
        l_eye = l_eye.reshape(-1, IMG_SIZE, IMG_SIZE, 3)
        # l_eye = np.expand_dims(l_eye,axis=0)
        lpred = model.predict(l_eye)
        if (np.argmax(lpred) == 2):
            lbl = 'Open'
        if (np.argmax(lpred) == 3):
            lbl = 'Closed'
        break

    try:
        if ((np.argmax(rpred) == 2) & (np.argmax(lpred) == 2)):
            score = score + 1
            cv2.putText(frame, "Closed", (10, height - 20), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
        else:
            score =score - 1
            cv2.putText(frame, "Open", (10, height - 20), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
    except ValueError:
        print("Can't get the relevant input. Please try again")
        break

    if (score < 0):
        score = 0
    cv2.putText(frame, 'Drowsiness:' + str(score), (300, height - 20), font, 1, (255, 255, 255), 1, cv2.LINE_AA)
    if (score > 10):
        # person is feeling sleepy so we beep the alarm
        try:
            sound.play()

        except:  # isplaying = False
            pass
        if (thicc < 16):
            thicc = thicc + 2
        else:
            thicc = thicc - 2
            if (thicc < 2):
                thicc = 2
        cv2.rectangle(frame, (0, 0), (width, height), (0, 0, 255), thicc)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):#To close the program, press q
        break
cap.release()
cv2.destroyAllWindows()