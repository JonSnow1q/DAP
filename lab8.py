import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

while True:
    i=GPIO.input(4)
    if i==True:
        print("Light is Off")
    else:
        print("Light is On")