import cv2
import numpy as np
from flask import Flask, app, render_template, Response
from functions import lighting_detector, viewing_distance_detector

app = Flask(__name__)

#cap = cv2.VideoCapture(0)

'''@app.route('/')
def index():
  return render_template('stopwatch.html')

@app.route('/check', methods = ["POST"])
def check():
    while True:
        _,img = cap.read()
        num1 = lighting_detector(img)
        value = viewing_distance_detector(img)

        if value > 300:
            num2 = 1
        else:
            num2 = 0

        if num1 == 1:
            popup1 = 'Poor lighting! Please check you room lighting!'
        else:
            popup1 = 'Lighting is perfect!'

        if num2 == 1:
            popup2 = 'You are too close to the screen. Please maintain some distance!'
        else:
            popup2 = 'You are sitting perfectly fine :) !'

        index = open("stopwatch.html").read().format(lighting = popup1, distance = popup2)
        return index'''

class Video:
    cap = cv2.VideoCapture(0)
    while True:
        _,img = cap.read()
        num1 = lighting_detector(img)
        value = viewing_distance_detector(img)

        if value > 300:
            num2 = 1
        else:
            num2 = 0

        if num1 == 1:
            popup1 = 'Poor lighting! Please check you room lighting!'
        else:
            popup1 = 'Lighting is perfect!'

        if num2 == 1:
            popup2 = 'You are too close to the screen. Please maintain some distance!'
        else:
            popup2 = 'You are sitting perfectly fine :) !'

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break

html = open('stopwatch.html','r').read().format(p = Video())
         

if __name__ == '__main__':
    app.run(debug=True)            