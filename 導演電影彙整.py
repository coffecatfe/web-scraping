import requests
from pyquery import PyQuery as pq

name = input().replace(' ','+')


url1 = 'https://www.imdb.com/find?ref_=nv_sr_fn&q={}&s=all'\
.format(name)
response = requests.get(url1)
#print (response.text)

doc = pq(response.text)
data = doc('#main > div > div:nth-child(3)> table ').find('a').eq(0)

url2 = data.attr.href
root = 'https://www.imdb.com'

url3 = root+url2
response = requests.get(url3)
doc = pq(response.text)

DirData = doc('div[data-category="director"]')
StrData = str(DirData.text())
index = StrData.rfind('(')
print (StrData[index+1:-1])


#print (DirData)

#print (DirData)
#<a name="director">Director</a> (9 credits)



DirData = DirData.next()


NameLst = []
YearLst = []

#for each in DirData.items():
#print (DirData)    

name = DirData("b")
for each in name.items():
    NameLst.append(each.text())

year = DirData("span")
for each in year.items():
    YearLst.append(each.text())

L = len(NameLst)


for i in range(L):
    if YearLst[i] != '':
        print (NameLst[i],YearLst[i],sep=',')
    else:
        print (NameLst[i])

