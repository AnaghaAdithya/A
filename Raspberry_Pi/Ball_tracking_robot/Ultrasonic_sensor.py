import RPi.GPIO as GPIO
import time
#import cv2
#hardware work
GPIO.setmode(GPIO.BOARD)

GPIO_TRIGGER = 33    #Left ultrasonic sensor
GPIO_ECHO = 35
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      
GPIO.output(GPIO_TRIGGER, False)
while(True):
    start=0
    stop=0
      # Set pins as output and input
       # Echo
     
      # Set trigger to False (Low)
    GPIO.output(GPIO_TRIGGER, False)
     
      # Allow module to settle
    time.sleep(0.01)
           
      #while distance > 5:
      #Send 10us pulse to trigger
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    begin = time.time()
    while GPIO.input(GPIO_ECHO)==0 and time.time()<begin+0.05:
        start = time.time()
     
    while GPIO.input(GPIO_ECHO)==1 and time.time()<begin+0.1:
        stop = time.time()
     
      # Calculate pulse length
    elapsed = stop-start
      # Distance pulse travelled in that time is time
      # multiplied by the speed of sound (cm/s)
    distance = elapsed * 34000
     
      # That was the distance there and back so halve the value
    distance = distance / 2
     
    print ("Distance : %.1f" % distance)
      # Reset GPIO settings
    time.sleep(1)

