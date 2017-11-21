import time
import requests
import random
myurl = "https://api.thingspeak.com/update?api_key=WS8CCAN4UMHDCQ0D&field1="

while True:
    url = myurl + str(random.randint(20, 80))
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        print("OK ", r.text)
    else:
        print("NOT OK ", r.status_code)
    time.sleep(20)
