import RPi.GPIO as GPIO  # Import GPIO library
import time


led1 = 10
ledr1 = 22

led2 = 15
ledr2 = 14

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(ledr1, GPIO.OUT)

GPIO.setup(led2, GPIO.OUT)
GPIO.setup(ledr2, GPIO.OUT)


def LED():
    for x in range(4):
        GPIO.output(led1, 1)
        GPIO.output(led2, 1)
        GPIO.output(ledr1, 0)
        GPIO.output(ledr2, 0)
        time.sleep(0.5)

        GPIO.output(ledr1, 1)
        GPIO.output(ledr2, 1)
        GPIO.output(led1, 0)
        GPIO.output(led2, 0)
        time.sleep(0.5)