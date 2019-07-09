from rrb3 import *
from random import randint
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
pin_extend=13
pin_retract=19

GPIO.setup(pin_extend, GPIO.OUT)
GPIO.setup(pin_retract, GPIO.OUT)

GPIO.output(pin_extend, GPIO.LOW)
GPIO.output(pin_retract, GPIO.LOW)


rr = RRB3(12, 12) # Battery voltage 12V, motor 12V
T = 20 # 20 seconds to extend
extended = False
GPIO.setwarnings(False)

try:
    while True:
        if GPIO.input(pin_extend):
        
            if rr.get_distance() < 20:
                if extended: # if extended retract and vice versa
                    print("retracting")
                    rr.set_led1(True) # LED 1 on
                    rr.reverse(T, 1.0)
                    rr.set_led1(False)
                    extended = False
                print("done retracting")

        elif not GPIO.input(pin_extend):
            if rr.get_distance()<20:
                if not extended:
                    print("extending")
                    rr.set_led2(True)
                    rr.forward(T, 1.0)
                    rr.set_led2(False)
                    extended = True

                print("done extending")

                

finally:
    rr.cleanup() # Set all GPIO pins to safe input state
    
                




