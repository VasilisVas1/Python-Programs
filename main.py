from urllib.request import Request, urlopen
import json
import urllib.request


req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()

k=json.loads(data.decode('utf-8'))
p=k['randomness']

f=[str(p)[i:i+2] for i in range (0,len(str(p)),2)]

g = []
for i in f:
  g.append(int(i,16)%80)

g=set(g)

url='https://api.opap.gr/draws/v3.0/1100/last-result-and-active'
response=urllib.request.urlopen(url)
html = response.read()
data=html.decode()
kino=json.loads(data)
kino['last']["winningNumbers"]['list']

opap=kino['last']["winningNumbers"]['list']

d=0
for x in g:
  for m in opap:
    if x==m :
      d=d+1

print("Οι αριθμοί που θα κληρωνόντουσαν στην τελευταία κλήρωση του κίνο είναι ",d)