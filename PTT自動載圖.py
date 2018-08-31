# --* coding:utf-8 *--

from urllib.request import urlretrieve 
from bs4 import BeautifulSoup 
import requests
import datetime
import re
import os

root = 'https://www.ptt.cc'

t = datetime.datetime.now()
today = '{}/{}'.format(t.month,t.strftime('%d'))
time = today
count = 0

url = 'https://www.ptt.cc/bbs/Beauty/index.html'
data = {}


while time == today:

    res = requests.get(url)
    soup = BeautifulSoup(res.text,'lxml')
    prePage = soup.find('a',string='‹ 上頁')['href']
    url = root+prePage
#==================================================================================
    #找出文章區塊
    
    if count == 0:
        line = soup.select('#main-container > \
    div.r-list-container.action-bar-margin.bbs-screen > div.r-list-sep')[0]
        temp = line.find_previous_siblings('div',{'class','r-ent'})
        count += 1
    else:
        temp = soup.findAll('div',{'class','r-ent'})[::-1]
        
#==================================================================================
    #找出標題、日期、推文數  
    for each in temp:
        try:
            title = each.find('a').text
        except AttributeError:
            continue
        time = each.find('div',{'class','date'}).text.strip()
        #print (time)
        if time != today:
            break
        
        push = each.find('div',{'class','nrec'}).text

        if push == '爆':
            push = 100
        try:
            push = int(push)
        except ValueError:
            push = -1 
        #print (push)
#==================================================================================
    #如果推文數超過某數量，才會把連結抓出來並執行下一步
        if push  >= 10:
            
            index = title.find(']')
            title = title[index+2:]
            
            link = root + each.find('a')['href']
            data[title]=link
            Imageroot = 'https://imgur.com'
            

#==================================================================================
    #以標題名稱創建資料夾
n=0               
for title in data:
    n += 1    
    print  (n)
    print (title)
    num = 0

    try:
        dir_name = r'C:/Users/A21C96410/Desktop/beauty/'+title
        if not os.path.exists(dir_name):    #先確認資料夾是否存在
            os.makedirs(dir_name)
    except OSError:
        dir_name = r"C:\Users\A21C96410\Desktop\beauty\others"
        if not os.path.exists(dir_name):    
            os.makedirs(dir_name)

#==================================================================================
    #將圖存入資料夾中
    ImgRes = requests.get(data[title])
    #print (data[title])
    ImgSoup = BeautifulSoup(ImgRes.text,'lxml')
    ImgLink = ImgSoup.select('div#main-container')[0].\
    findAll('a',target='_blank',\
    string=re.compile('^https://(i.|)imgur.com/.+(\.jpg)$'))
                
    ImgLocation = set()
                
    for eachImg in ImgLink:
        ImgLocation.add(eachImg.text)

    ImgLocation = list(ImgLocation)      
    for Img in ImgLocation:
        num += 1
        print (num,Img)
            #urlretrieve (Img, r"{}\{:0>3d}.jpg".format(dir_name,num))


