import os
import picamera
import time

def take_photo():
    path = './pic/{}/'.format(str(datetime.date.today()))
    folder = os.path.exists(path)
    if not folder: os.makedirs(path)
    
    camera = picamera.PiCamera()
    # camera.rotation = 180
    time.sleep(0.5)  # Camera warm-up time
    camera.capture('./pic/{}/test_{}.jpg'.format(str(datetime.date.today(), round(time.time()))))

def recording():
    camera = picamera.PiCamera()
    camera.start_recording('video_test.h264')
    while 1:
        camera.wait_recording()
        n = input('wait for stop:')
        if n == 'y': camera.stop_recording()
        exit()


if __name__ == "__main__":
    take_photo()