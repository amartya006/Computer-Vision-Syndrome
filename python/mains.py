import cv2
import json
import numpy as np
from functions import lighting_detector, screen_brightness

cap = cv2.VideoCapture(0)

'''def write_json(new_data, filename='mydata.json'):

    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["Details"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 2)'''

while True:
    _,img = cap.read()
    x = lighting_detector(img)
    y = screen_brightness()

    if y > 40:
        num2 = 1
    else:
        num2 = 0
    if x==1 or num2 ==1:
        dictionary = {
            "Lighting" : x,
            "Brightness" : num2
        }
        #write_json(dictionary)
        with open("python\mydata.json", "w") as outfile:
            json.dump(dictionary, outfile)

        dictionary.clear()

    if cv2.waitKey(1) % 0xFF == ord('q'):
        break
