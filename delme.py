import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
import time
import sys

ledpin = 15

 # abov hereis alwasem,    above here is always the same

 # output mode for pin
GPIO.setup(ledpin, GPIO.OUT)

 # set pin low
GPIO.output(ledpin, GPIO.HIGH )


GPIO.output(ledpin, GPIO.LOW )



while True:



    key = sys.stdin.read(1)

    if key == 'p':
        GPIO.output(ledpin, GPIO.LOW )
    elif key == 'o':
        GPIO.output(ledpin, GPIO.HIGH )
    elif key == 'q':
        GPIO.output(ledpin, GPIO.HIGH )
    elif key == 'w':
        GPIO.output(ledpin, GPIO.HIGH )
    elif key == '\n':
        pass  # do nothing
    else:
        print('what you say?')
