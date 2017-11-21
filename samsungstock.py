import time
from datetime import datetime
import requests

def extract(data):
    i = data.find("<dd>현재가 ")
    if i > 0:
        line = data[i:i+100]
        line = line.split(" ")
        with open("삼성주식추적.txt", "a") as f:
            print(datetime.now().strftime('%Y-%m-%d %H:%M:%S '), "삼성전자주식", line[1], file=f)
            print(datetime.now().strftime('%Y-%m-%d %H:%M:%S '), "삼성전자주식", line[1])
    else:
        print(r.status, "got", len(data), "types")


url = 'http://finance.naver.com/item/frgn.nhn?code=005930'
r = requests.get(url)
if r.status_code == requests.codes.ok:
    extract(r.text)
else:
    print("NOT OK ", r.status_code)



