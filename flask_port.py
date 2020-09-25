# -*- coding: utf-8 -*-
'''
raise a port for executing GPIO functions

'''
from flask import Flask ,request
import RPi.GPIO as GPIO
import picamera
import time
import threading
from get_app import get_main_func



GPIO.setmode(GPIO.BCM)
led_pin = 4
GPIO.setup(led_pin, GPIO.OUT)
valve_pin = 17
GPIO.setup(valve_pin, GPIO.OUT)



app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello Flask'


#
@app.route('/whiskyget' ,methods=['POST'])
def whiskyget():
    get_main_func()
    # tmp_lst = list(dict(request.form).values())
    # target=camera_shot(tmp_lst)
    # threading.Thread(target=led_light).start()
    # threading.Thread(target=valve_start).start()
    # threading.Thread(target=camera_shot(tmp_lst)).start()


    return 'led'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 80)
