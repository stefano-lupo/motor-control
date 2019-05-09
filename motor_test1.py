from time import sleep
import RPi.GPIO as GPIO



DIR = 21   # Direction GPIO Pin
STEP = 20  # Step GPIO Pin
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 20000   # Steps per Revolution (360 / 7.5)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)                                                                                                 
GPIO.output(DIR, CW)

step_count = SPR
delay = 0.0004
# GPIO.output(DIR, GPIO.HIGH)
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)
    print(x)
# sleep(.5)
# GPIO.output(DIR, CCW)
# for x in range(step_count):
#     GPIO.output(STEP, GPIO.HIGH)
#     sleep(delay)
#     GPIO.output(STEP, GPIO.LOW)
#     sleep(delay)

GPIO.cleanup()