import numpy as np
import cv2
from keras.models import load_model
import time


class_names = ['baked_potato', 'burger', 'crispy_chicken', 'donut', 'fries', 'hotdog', 'pizza', 'sandwich', 'taco', 'shawarma']

def print_class(data):
    data_ = data
    data_out1 = data[0,0]
    data_out = 0
    print(data)
    for i in range(10):
        if data_out1 < data_[0,i]:
            data_out = i
            data_out1 = data[0,i]
    print(data_[0,data_out])
    if data_out == 0:
        return 'baked potato'
    if data_out == 1:
        return 'burger'
    if data_out == 2:
        return 'crispy chiken'
    if data_out == 3:
        return 'donut'
    if data_out == 4:
        return 'fries'
    if data_out == 5:
        return 'hotdog'
    if data_out == 6:
        return 'pizza'
    if data_out == 7:
        return 'sandwich'
    if data_out == 8:
        return 'taco'
    if data_out == 9:
        return 'shawarma'

image = np.zeros((800,1000,3), np.uint8)

	
# Window name in which image is displayed 
window_name = 'Image'

# font 
font = cv2.FONT_HERSHEY_SIMPLEX 

# org 
otstup = 150
org = (50, otstup) 
org1 = (50, 400) 
# fontScale 
fontScale = 5

# Blue color in BGR 
color = (255, 255, 255) 
balans =2000
# Line thickness of 2 px 
thickness = 3
cv2.imshow("food", image) 
model2= load_model('project.h5')
cap = cv2.VideoCapture(0)

while(True):
# Capture frame-by-frame
    ret, frame = cap.read()
    #print(frame.shape)
    if ret == True:
        #cv2.imshow('first tarelka',frame)
        if cv2.waitKey(33) == ord('d'):

            tarelka = cv2.resize(frame,(256,256))
            #cv2.imshow('first tarelka',frame)

            mmm = model2.predict(np.reshape(tarelka,(1,256,256,3)))
            name = print_class(mmm)
            image = cv2.putText(image, name, org, font, 
				fontScale, color, thickness, cv2.LINE_AA) 
            otstup = otstup + 150
            org = (50, otstup)
            cv2.imshow("food", image) 
            time.sleep(1)
        cv2.imshow("video", frame) 
    if cv2.waitKey(33) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
