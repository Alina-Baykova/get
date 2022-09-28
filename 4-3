import RPi.GPIO as GPIO
GPIO.setmode (GPIO.BCM)
dac=[26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
#GPIO.output(dac, [1,1,1,1,1,1,1,1])

led=22
GPIO.setup(led, GPIO.OUT)
pwm=GPIO.PWM(led,1000)
pwm.start (0)

try:
    while True:
        DutyCicle = int(input())
        pwm.ChangeDutyCycle(100-DutyCicle)
        print(3.3*DutyCicle/100)

finally:
    GPIO.setup(led, 0)
    GPIO.setup(dac, 0)
    GPIO.cleanup()
