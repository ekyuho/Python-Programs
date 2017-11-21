import datetime, time
import urllib.request

url = "http://news.joins.com/article/21844194"

f = urllib.request.urlopen(url)
#data = f.read().decode('euc-kr')
data = f.read().decode('utf-8')

begin = data.find("존경하는 국민 여러분")
end = data.find("감사합니다.")

end += len("감사합니다.")
print("total=", len(data))
print("begin=", begin)
print(data[begin:begin+100])
print(data[end-100:end])
print("length=", end-begin)

speech = data[begin:end]
speech = speech.split()
#print(speech[:100])

analyze = {}
for word in speech:
    analyze[word] = analyze.get(word, 0) + 1

flist = sorted(analyze.items(), key=lambda kv: kv[1], reverse=True)
print("number of words is ", len(flist))

cnt = 0
for k, v in flist:
    print(k, v)
    if cnt > 100: break
    cnt += 1
