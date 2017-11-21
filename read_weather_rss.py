import datetime, time
import urllib.request
import re

f = urllib.request.urlopen('http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1144060000')
data = str(f.read())

pat = re.compile(r"<tm>(\d*)<\/tm>")
m = pat.search(str(data))
if m:
    dd = m.group(1)
    d2 = dd[0:4]+"-"+dd[4:6]+"-"+dd[6:8]+" "+dd[8:10]+":"+dd[10:12]
else:
    dd = "no data"

pat = re.compile(r"<hour>(\d*)<\/hour>\\n\s*<day>(\d*)<\/day>\\n\s*<temp>([-\.\d]*)<\/temp>")
m = pat.search(str(data))
if not m:
    print("no data")
else:
    hh = m.group(1) + ":00"
    temp = m.group(3)

    print("현재시간은 ", d2)
    print(hh, "시의 예측온도는 ", temp)
