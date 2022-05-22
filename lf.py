import RPi.GPIO as GPIO  # Import GPIO library
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

ls = 23
ms = 24
rs = 25

GPIO.setup(ls, GPIO.IN)
GPIO.setup(ms, GPIO.IN)
GPIO.setup(rs, GPIO.IN)

i2c = board.I2C()
sensor = adafruit_tcs34725.TCS34725(i2c)



color = sensor.color
color_rgb = sensor.color_rgb_bytes

HEX = "#{0:02X}".format(color)

print("RGB color as 8 bits per channel int: #{0:02X} or as 3-tuple: {1}".format(color, color_rgb))
RGB = ("{0}, {1}, {2}".format(*color_rgb))

a = int(RGB.split(",")[0])
b = int(RGB.split(",")[1])
c = int(RGB.split(",")[2])

def main():
    p1.start(0)
    p2.start(0)

    stop()
    p1.ChangeDutyCycle(75)
    p2.ChangeDutyCycle(75)

    GPIO.output(en1, 1)
    GPIO.output(en2, 1)

    forward()
    time.sleep(2)

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
            p1.ChangeDutyCycle(75)
            p2.ChangeDutyCycle(75)
            GPIO.output(en1, 1)
            GPIO.output(en2, 1)

            time.sleep(2)
        else:
            if GPIO.input(ls):
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
                p1.ChangeDutyCycle(50)
                p2.ChangeDutyCycle(50)

                GPIO.output(en1, 1)
                GPIO.output(en2, 1)

                time.sleep(2)
            elif GPIO.input(rs):
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
                p1.ChangeDutyCycle(50)
                p2.ChangeDutyCycle(50)

                GPIO.output(en1, 1)
                GPIO.output(en2, 1)

                time.sleep(2)
            elif not GPIO.input(ms):

                stop()
                GPIO.output(ledr1, 1)
                GPIO.output(led1, 0)
                GPIO.output(ledr2, 1)
                GPIO.output(led2, 0)
                colorsensors()
                if HEX != "#00":
                    if a < 125 and a == b == c:
                        print("Something is wrong.")
                        break

                    elif a >= 125 and a == b == c:
                        print("Go back to the beginning.")
                        break

                    elif 0 < a < 70 and b > 70 and c > 70:
                        print("You've reached the first station.")

                    elif a > 70 and b > 30 and c < 25:
                        print("You've reached the last station.")

                    elif a > 70 and b < 25 and c < 25:
                        print("You've reached the second station.")

                    else:
                        print("undetected color")
                        break

                else:
                    print("failure")
                time.sleep(1)





main()

