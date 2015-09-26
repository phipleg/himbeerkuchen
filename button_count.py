"""Button count - Listens for input on GPIO 6 and prints the counted events""" 
import RPi.GPIO as GPIO
import time


PIN=6
GPIO.setmode(GPIO.BCM)

count = 0
def on_switch(pin):
    global count
    count += 1
    print count

GPIO.setup(6, GPIO.IN)
GPIO.add_event_detect(PIN, GPIO.FALLING, bouncetime=200)
GPIO.add_event_callback(PIN, on_switch) 

if __name__ == '__main__':
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        pass
    GPIO.cleanup()
