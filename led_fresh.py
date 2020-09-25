import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led_pin = 4
GPIO.setup(led_pin, GPIO.OUT)

for i in range(3):
    GPIO.output(led_pin, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(led_pin, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(led_pin, GPIO.HIGH)
