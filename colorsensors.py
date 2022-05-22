import RPi.GPIO as GPIO
import time
import adafruit_tcs34725
import board

GPIO.setmode(GPIO.BCM)

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


