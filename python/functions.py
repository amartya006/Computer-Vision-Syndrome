import cv2
import numpy as np
import os
import screen_brightness_control as sbc

#cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

faceCascade = cv2.CascadeClassifier(r'python\haarcascade_frontalface_default.xml')

def lighting_detector(img):

    img = np.array(img)
    for i in img:
        for j in i:
            sum = 0
            for k in j:
                sum = sum + k

    if int(sum/3) < 30:
        return 1
    else:
        return 0                

def screen_brightness():

    current_brightness = sbc.get_brightness()
    return current_brightness

