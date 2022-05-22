import RPi.GPIO as GPIO  # Import GPIO library
import time
import adafruit_tcs34725
import board


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


#setting up the LED
led1 = 10
ledr1 = 22

led2 = 15
ledr2 = 14

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(ledr1, GPIO.OUT)

GPIO.setup(led2, GPIO.OUT)
GPIO.setup(ledr2, GPIO.OUT)


#Setting up the motors
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


# setting up the ultrasonic sensors
TRIG = 17
ECHO = 18
TRIG1 = 26
ECHO1 = 19

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(TRIG1, GPIO.OUT)
GPIO.setup(ECHO1, GPIO.IN)

#setting up the MH sensors series
ls = 23
ms = 24
rs = 25

GPIO.setup(ls, GPIO.IN)
GPIO.setup(ms, GPIO.IN)
GPIO.setup(rs, GPIO.IN)


#setting up the colorsensor
i2c = board.I2C()
sensor = adafruit_tcs34725.TCS34725(i2c)


#defining LED function
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

#defining all of the motor functions
def stop():
    GPIO.output(m11, 0)
    GPIO.output(m12, 0)
    GPIO.output(m21, 0)
    GPIO.output(m22, 0)

    GPIO.output(m31, 0)
    GPIO.output(m32, 0)
    GPIO.output(m41, 0)
    GPIO.output(m42, 0)
    print("Stop")


def forward():
    GPIO.output(m11, 1)
    GPIO.output(m12, 0)
    GPIO.output(m21, 1)
    GPIO.output(m22, 0)

    GPIO.output(m31, 1)
    GPIO.output(m32, 0)
    GPIO.output(m41, 1)
    GPIO.output(m42, 0)
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
    GPIO.output(m11, 1)
    GPIO.output(m12, 0)
    GPIO.output(m21, 0)
    GPIO.output(m22, 0)

    GPIO.output(m31, 0)
    GPIO.output(m32, 0)
    GPIO.output(m41, 1)
    GPIO.output(m42, 0)
    print("Left")


def right():
    GPIO.output(m11, 0)
    GPIO.output(m12, 0)
    GPIO.output(m21, 1)
    GPIO.output(m22, 0)

    GPIO.output(m31, 1)
    GPIO.output(m32, 0)
    GPIO.output(m41, 0)
    GPIO.output(m42, 0)

    print("Right")


def sright():
    GPIO.output(en1, 0)
    GPIO.output(en2, 0)

    GPIO.output(m11, 1)
    GPIO.output(m12, 0)
    GPIO.output(m41, 1)
    GPIO.output(m42, 0)
    p1.ChangeDutyCycle(25)

    GPIO.output(en1, 1)

    GPIO.output(m21, 1)
    GPIO.output(m22, 0)
    GPIO.output(m31, 1)
    GPIO.output(m32, 0)
    p2.ChangeDutyCycle(0)

    GPIO.output(en2, 1)

    print("Slightly Right")


def sleft():
    GPIO.output(en1, 0)
    GPIO.output(en2, 0)

    GPIO.output(m11, 1)
    GPIO.output(m12, 0)
    GPIO.output(m41, 1)
    GPIO.output(m42, 0)
    p1.ChangeDutyCycle(0)

    GPIO.output(en1, 1)

    GPIO.output(m21, 1)
    GPIO.output(m22, 0)
    GPIO.output(m31, 1)
    GPIO.output(m32, 0)
    p2.ChangeDutyCycle(25)

    GPIO.output(en2, 1)

    print("Slightly Left")


#defining the linefolloing part with the colorsensor part
def lf():
    p1.start(0)
    p2.start(0)

    stop()
    p1.ChangeDutyCycle(25)
    p2.ChangeDutyCycle(25)

    GPIO.output(en1, 1)
    GPIO.output(en2, 1)

    forward()
    time.sleep(1.5)
    stop()

    while True:
        if GPIO.input(ms) and not GPIO.input(ls) and not GPIO.input(rs):
            print("On the right path!")

            GPIO.output(led1, 1)
            GPIO.output(ledr1, 0)
            GPIO.output(led2, 1)
            GPIO.output(ledr2, 0)

            GPIO.output(en1, 0)
            GPIO.output(en2, 0)

            forward()
            p1.ChangeDutyCycle(25)
            p2.ChangeDutyCycle(25)
            GPIO.output(en1, 1)
            GPIO.output(en2, 1)

            time.sleep(2)
        else:
            if GPIO.input(ls):
                stop()
                print("ALERT: Left wheels are on the black line!")
                GPIO.output(ledr1, 1)
                GPIO.output(led1, 0)
                GPIO.output(ledr2, 1)
                GPIO.output(led2, 0)

                GPIO.output(en1, 0)
                GPIO.output(en2, 0)

                sleft()
                print("Fixed the left wheel because it was on the black line.")
                time.sleep(2)

                GPIO.output(en1, 0)
                GPIO.output(en2, 0)

                forward()
                p1.ChangeDutyCycle(25)
                p2.ChangeDutyCycle(25)

                GPIO.output(en1, 1)
                GPIO.output(en2, 1)

                time.sleep(2)
            elif GPIO.input(rs):
                stop()
                print("ALERT: Right wheels are on the black line!")
                GPIO.output(ledr1, 1)
                GPIO.output(led1, 0)
                GPIO.output(ledr2, 1)
                GPIO.output(led2, 0)

                GPIO.output(en1, 0)
                GPIO.output(en2, 0)

                sright()
                print("Fixed the right wheel because it was on the black line.")
                time.sleep(2)

                GPIO.output(en1, 0)
                GPIO.output(en2, 0)

                forward()
                p1.ChangeDutyCycle(25)
                p2.ChangeDutyCycle(25)

                GPIO.output(en1, 1)
                GPIO.output(en2, 1)

                time.sleep(2)
            elif not GPIO.input(ms):

                stop()
                GPIO.output(ledr1, 1)
                GPIO.output(led1, 0)
                GPIO.output(ledr2, 1)
                GPIO.output(led2, 0)

                color = sensor.color
                color_rgb = sensor.color_rgb_bytes

                HEX = "#{0:02X}".format(color)
                RGB = ("{0}, {1}, {2}".format(*color_rgb))

                a = int(RGB.split(",")[0])
                b = int(RGB.split(",")[1])
                c = int(RGB.split(",")[2])
                if HEX != "#00":
                    if a < 125 and a == b == c:
                        print("Something is wrong.")
                        break

                    elif a >= 125 and a == b == c:
                        print("Go back to the beginning.")
                        break

                    elif (0 < a < 70 and b > 70 and c > 70) or (0 < a < 70 and b == c):
                        print("You've reached the first station.")
                        answer1 = input("If you want to continue type Y, if not type N.")
                        if answer1 == "Y":
                            print("We're going forward.")
                            forward()
                            continue
                        elif answer1 == "N":
                            print("We're stopping.")
                            stop()
                            break
                        else:
                            print("Something went wrong. Please try again.")
                            break


                    elif a > 70 and b > 30 and c < 25:
                        print("You've reached the last station.")
                        answer2 = input("If you want to continue type Y, if not type N.")
                        if answer2 == "Y":
                            print("We're going forward.")
                            forward()
                            continue
                        elif answer2 == "N":
                            print("We're stopping.")
                            stop()
                            break
                        else:
                            print("Something went wrong. Please try again")
                            break


                    elif a > 70 and b < 25 and c < 25:
                        print("You've reached the second station.")
                        answer3 = input("If you want to continue type Y, if not type N")
                        if answer3 == "Y":
                            print("We're going forward.")
                            forward()
                            continue
                        elif answer3 == "N":
                            print("We're stopping.")
                            stop()
                            break
                        else:
                            print("Something went wrong. Please try again.")
                            break

                    else:
                        print("undetected color", RGB)
                        break

                else:
                    print("failure")
                time.sleep(1)

#defining the main function
def main():
    LED()
    p1.start(0)
    p2.start(0)

    stop()
    p1.ChangeDutyCycle(25)
    p2.ChangeDutyCycle(25)

    GPIO.output(en1, 1)
    GPIO.output(en2, 1)

    forward()
    time.sleep(2)
    stop()
    count = 0
    while count < 31:
        avgDistance = 0
        avgDistance1 = 0
        for i in range(5):
            GPIO.output(TRIG, False)
            GPIO.output(TRIG1, False)
            time.sleep(0.1)

            GPIO.output(TRIG, True)
            GPIO.output(TRIG1, True)
            time.sleep(0.00001)
            GPIO.output(TRIG, False)
            GPIO.output(TRIG1, False)

            while GPIO.input(ECHO) == 0:
                GPIO.output(led1, 0)
                GPIO.output(led2, 0)
            pulse_start = time.time()

            while GPIO.input(ECHO) == 1:
                GPIO.output(led1, 1)
                GPIO.output(led2, 1)
            pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start

            distance = pulse_duration * 17150
            distance = round(distance, 2)
            avgDistance = avgDistance + distance

            avgDistance = avgDistance / 5
            print("Left sensor:", avgDistance)

            GPIO.output(TRIG1, False)
            time.sleep(0.1)

            GPIO.output(TRIG1, True)
            time.sleep(0.00001)
            GPIO.output(TRIG1, False)

            while GPIO.input(ECHO1) == 0:
                GPIO.output(led1, 0)
                GPIO.output(led2, 0)
            pulse_start1 = time.time()

            while GPIO.input(ECHO1) == 1:
                GPIO.output(led1, 1)
                GPIO.output(led2, 1)
            pulse_end1 = time.time()
            pulse_duration1 = pulse_end1 - pulse_start1

            distance1 = pulse_duration1 * 17150
            distance1 = round(distance1, 2)
            avgDistance1 = avgDistance1 + distance1

            avgDistance1 = avgDistance1 / 5
            print("Right sensor:", avgDistance1)

            p1.start(0)
            p2.start(0)

            stop()
            time.sleep(3)

            p1.ChangeDutyCycle(25)
            p2.ChangeDutyCycle(25)

            forward()


            GPIO.output(en1, 1)
            GPIO.output(en2, 1)
            time.sleep(1)

            count = count + 1
            if avgDistance1 < 15:
                stop()
                print("ALERT: Right sensor has encountered an object!")
                GPIO.output(led1, 0)
                GPIO.output(ledr1, 1)
                GPIO.output(led2, 0)
                GPIO.output(ledr2, 1)

                stop()
                time.sleep(1)
                back()
                time.sleep(1.5)
                sright()
                time.sleep(1.5)
                stop()
                time.sleep(1)

            elif avgDistance < 15:
                stop()
                print("ALERT: Left sensor has encountered an object!")
                GPIO.output(led1, 0)
                GPIO.output(ledr1, 1)
                GPIO.output(led2, 0)
                GPIO.output(ledr2, 1)

                stop()
                time.sleep(1)
                back()
                time.sleep(1.5)

                sleft()
                time.sleep(1.5)
                stop()
                time.sleep(1)

            else:
                lf()


main()
