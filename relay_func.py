import RPi.GPIO as GPIO
import time


def relay_run():
    GPIO.setmode(GPIO.BCM)
    relay_pin = 18
    GPIO.setup(relay_pin, GPIO.OUT)

    for i in range(1):
        GPIO.output(relay_pin, GPIO.HIGH)
        time.sleep(4.5)
        GPIO.output(relay_pin, GPIO.LOW)
        time.sleep(1)
    GPIO.cleanup()


if __name__ == "__main__":
    relay_run()
