
from pyquery import PyQuery as pq
import requests

total = 0
while True:
    try:
        data = input().split()

        date = data[0].split('/')
        Y = date[0]
        M = date[1]
        D = date[2]

        country = data[1]
        cost = int(data[2])

        
        url = 'https://rate.bot.com.tw/xrt/quote/{}-{}/{}'.format(Y,M,country)
        response = requests.get(url)
        #print (response.text)

        doc = pq(response.text)
        rate = doc('a').filter(lambda i: pq(this).text() == data[0]).parent()\
         .siblings().eq(4).text()
        rate = float(rate)

        total += round(rate*cost)
    except EOFError:
        break

print (total)


