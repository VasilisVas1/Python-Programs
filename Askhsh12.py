from urllib.request import Request, urlopen
import json

req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()

k=json.loads(data.decode('utf-8'))
l=k['round']
p=k['randomness']

#The last 100 rounds and their randomness
for i in range(1,100):
    req = Request('https://drand.cloudflare.com/public/' + str(l-1), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    k = json.loads(data.decode('utf-8'))
    l=k['round']
    p=p+k['randomness']

max1=0
max2=0
k=bin(int(p,16))
mhden=k.split("1")
asoi=k.split("0")
for i in mhden:
    if len(i)>max1:
        max1=len(i)

for i in asoi:
    if len(i)>max2:
        max2=len(i)

print("Η μεγαλύτερη ακολουθία απο συνεχόμενα μηδενικά είναι :",max1)
print("Η μεγαλύτερη ακολουθία απο συνεχόμενους άσους είναι :",max2)