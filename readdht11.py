import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin gpio2 and gpio3
s1 = dht11.DHT11(pin=2)
s2 = dht11.DHT11(pin=3)

while True:
    r1 = s1.read()
    r2 = s2.read()
    if not (r1.is_valid() and r2.is_valid()): continue
    
    print("Temperature: (", r1.temperature, r2.temperature, ")", 
    "Humidity: (", r1.humidity, r2.humidity,  ")")

    time.sleep(1)
