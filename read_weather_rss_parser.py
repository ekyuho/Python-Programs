import feedparser
import xml.etree.ElementTree as ET

d = feedparser.parse("http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4113552000")
d = "<Doc>" + d.entries[0]["summary"] +"</body></Doc>"
d = ET.fromstring(d)
t = d.find('header').find('tm').text
print("At %s %s"%(t[:8], t[8:]))
for k in d.iter('data'):
    print("%2d. %2d00 T=%4.1f H=%d"%(int(k.get('seq')), int(k.find('hour').text), float(k.find('temp').text), int(k.find('reh').text)))
