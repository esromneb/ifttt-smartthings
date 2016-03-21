import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
import time


ledpin = 15

 # abov hereis alwasem,    above here is always the same

 # output mode for pin
GPIO.setup(ledpin, GPIO.OUT)

 # set pin low
GPIO.output(ledpin, GPIO.HIGH )


GPIO.output(ledpin, GPIO.LOW )



print 'Hello World'



for x in range(0,3):

    print 'high is off'
    GPIO.output(ledpin, GPIO.HIGH )

    time.sleep(0.3)

    print 'low is on'
    GPIO.output(ledpin, GPIO.LOW )

    time.sleep(0.3)


    if ledpin == 4:
        print 'the world is ok'
    else:
        print 'one'
        print 'two'
        print 'three'
    print 'always runs no matter what the if was'

    print x



GPIO.output(ledpin, GPIO.HIGH )
print 'last this is turn it off'
