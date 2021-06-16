'''
drive buzzer by setting GPIO
tunning musical scale by setting p.ChangeFrequency
de re   me fa   so la si
523 587 659 698 784 880 988
1046 1175 1318 1397 1568 1760 1976
'''

import time
import RPi.GPIO as GPIO


def littleBee():
    GPIO.setmode(GPIO.BCM)
    buzzer_pin = 5
    GPIO.setup(buzzer_pin, GPIO.OUT)
    p = GPIO.PWM(buzzer_pin, 50)
    p.start(50)

    p.ChangeFrequency(784)
    time.sleep(0.5)
    p.ChangeFrequency(659)
    time.sleep(0.5)
    p.ChangeFrequency(659)
    time.sleep(0.5)
    p.ChangeFrequency(598)
    time.sleep(0.5)
    p.ChangeFrequency(587)
    time.sleep(0.5)
    p.ChangeFrequency(587)
    time.sleep(0.5)
    p.ChangeFrequency(523)
    time.sleep(0.5)
    p.ChangeFrequency(587)
    time.sleep(0.5)
    p.ChangeFrequency(659)
    time.sleep(0.5)
    p.ChangeFrequency(598)
    time.sleep(0.5)
    p.ChangeFrequency(784)
    time.sleep(0.5)
    p.ChangeFrequency(784)
    time.sleep(0.5)
    p.ChangeFrequency(784)
    time.sleep(0.5)

    p.stop()
    GPIO.cleanup()


def familymart_ringo():
    GPIO.setmode(GPIO.BCM)
    bizz_pin = 5
    GPIO.setup(bizz_pin, GPIO.OUT)
    p = GPIO.PWM(bizz_pin, 50)
    p.start(50)
    # de re   me fa   so la si
    #523 587 659 698 784 880 988
    #1046 1175 1318 1397 1568 1760 1976
    p.ChangeFrequency(1318)
    time.sleep(0.5)
    p.ChangeFrequency(1046)
    time.sleep(0.5)
    p.ChangeFrequency(784)
    time.sleep(0.5)
    p.ChangeFrequency(1046)
    time.sleep(0.5)
    p.ChangeFrequency(1175)
    time.sleep(0.5)
    p.ChangeFrequency(1568)
    time.sleep(0.8)

    p.ChangeFrequency(1175)
    time.sleep(0.5)
    p.ChangeFrequency(1318)
    time.sleep(0.5)
    p.ChangeFrequency(1175)
    time.sleep(0.5)
    p.ChangeFrequency(784)
    time.sleep(0.5)
    p.ChangeFrequency(1046)
    time.sleep(0.7)


    p.stop()
    GPIO.cleanup()

if __name__ == "__main__":
    # littleBee()
    familymart_ringo()