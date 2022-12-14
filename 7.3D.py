import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LED = 38
TRIG = 11
ECHO = 16

max_distance = 20

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

led = GPIO.PWM(LED, 100)
led.start(0)

def calculate_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == False:
        start = time.time()

    while GPIO.input(ECHO) == True:
        end = time.time()

    sig_time = end-start
    
    distance = sig_time / 0.000058
    return distance

try:
    while 1:
        dist = calculate_distance()
        print(dist)
        if dist <= max_distance:
            led.change_duty_cycle(100 - (dist/max_distance * 100))
            time.sleep(0.1)
        else:
            led.change_duty_cycle(0)
            
except KeyboardInterrupt:
    print("Stopped Forcefully!")

led.stop()
GPIO.cleanup()