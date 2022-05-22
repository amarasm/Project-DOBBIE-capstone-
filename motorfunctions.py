import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO. BCM)

en1=13
m21=16
m22=5
m11=20
m12=21

en2=12
m31=9
m32=11
m41=7
m42=8


GPIO.setup(m11, GPIO.OUT)
GPIO.setup(m12, GPIO.OUT)
GPIO.setup(m21, GPIO.OUT)
GPIO.setup(m22, GPIO.OUT)

GPIO.setup(m31, GPIO.OUT)
GPIO.setup(m32, GPIO.OUT)
GPIO.setup(m41, GPIO.OUT)
GPIO.setup(m42, GPIO.OUT)



GPIO.setup(en1, GPIO.OUT)
GPIO.setup(en2, GPIO.OUT)
p1=GPIO.PWM(en1, 100)
p2=GPIO.PWM(en2, 100)


def stop():
    GPIO.output (m11, 0)
    GPIO.output (m12, 0)
    GPIO.output (m21, 0)
    GPIO.output (m22, 0)


    GPIO.output (m31, 0)
    GPIO.output (m32, 0)
    GPIO.output (m41, 0)
    GPIO.output (m42, 0)
    print("Stop")

def forward():
    GPIO.output (m11, 1)
    GPIO.output (m12, 0)
    GPIO.output (m21, 1)
    GPIO.output (m22, 0)

    GPIO.output (m31, 1)
    GPIO.output (m32, 0)
    GPIO.output (m41, 1)
    GPIO.output (m42, 0)
    print("Forward")

def back():
    GPIO.output(m11, 0)
    GPIO.output(m12, 1)
    GPIO.output(m21, 0)
    GPIO.output(m22, 1)

    GPIO.output(m31, 0)
    GPIO.output(m32, 1)
    GPIO.output(m41, 0)
    GPIO.output(m42, 1)
    print("Back")


def left():
    GPIO.output (m11, 1)
    GPIO.output (m12, 0)
    GPIO.output (m21, 0)
    GPIO.output (m22, 0)

    GPIO.output (m31, 0)
    GPIO.output (m32, 0)
    GPIO.output (m41, 1)
    GPIO.output (m42, 0)
    print("Left")

def right():
    GPIO.output (m11, 0)
    GPIO.output (m12, 0)
    GPIO.output (m21, 1)
    GPIO.output (m22, 0)


    GPIO.output (m31, 1)
    GPIO.output (m32, 0)
    GPIO.output (m41, 0)
    GPIO.output (m42, 0)

    print("Right")


def sright() :
    GPIO.output (en1, 0)
    GPIO.output (en2, 0)


    GPIO.output (m11, 1)
    GPIO.output (m12, 0)
    GPIO.output (m41, 1)
    GPIO.output (m42, 0)
    p1.ChangeDutyCycle(75)

    GPIO.output (en1, 1)

    GPIO.output (m21, 1)
    GPIO.output (m22, 0)
    GPIO.output (m31, 1)
    GPIO.output (m32, 0)
    p2.ChangeDutyCycle(25)


    GPIO.output (en2, 1)

    print("Slightly Right")

def sleft() :
    GPIO.output (en1, 0)
    GPIO.output (en2, 0)


    GPIO.output (m11, 1)
    GPIO.output (m12, 0)
    GPIO.output (m41, 1)
    GPIO.output (m42, 0)
    p1.ChangeDutyCycle(25)


    GPIO.output (en1, 1)


    GPIO.output (m21, 1)
    GPIO.output (m22, 0)
    GPIO.output (m31, 1)
    GPIO.output (m32, 0)
    p2.ChangeDutyCycle(75)

    GPIO.output (en2, 1)

    print("Slightly Left")