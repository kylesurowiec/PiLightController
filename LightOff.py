import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pinList = [2]

for i in pinList: 
    GPIO.setwarnings(False)
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

def trigger() :
        for i in pinList:
          GPIO.output(i, GPIO.LOW)
#         GPIO.cleanup()
          break
try: 
    trigger()
         
except KeyboardInterrupt:
  print "  Quit" 
  GPIO.cleanup()