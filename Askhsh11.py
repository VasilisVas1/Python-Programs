from urllib.request import Request, urlopen
import json
from scipy.stats import entropy as en
import pandas as pd


req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()

k=json.loads(data.decode('utf-8'))
l=k['round']
p=k['randomness']

#The last 20 rounds and their randomness
for i in range(1,20):

    req = Request('https://drand.cloudflare.com/public/' + str(l-1), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
    data = urlopen(req).read()
    k = json.loads(data.decode('utf-8'))
    l=k['round']
    p=p+k['randomness']

r=str(int(p,16))

g=[]
for i in r:
    g.append(i)

#finding the entropy of g
g = pd.Series(g)
data=en(g.value_counts())
print("The entropy is: ",data)