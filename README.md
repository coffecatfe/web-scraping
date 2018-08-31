# web-scraping
透過網路爬蟲來完成特定資料搜尋以及自動下載之功能 <br />

注意事項： <br />
● 需要安裝PyQuery,BeaufifulSoup,resquest,datetime....等套件 <br />
● 程式碼中檔案開啟或存取路徑需根據不同使用者做適度的修改 <br />


介紹： <br />
【PTT自動載圖】 <br />
● 將PTT中(ex:表特版)當日推文數超過預設值的文章裡的圖片自動下載到以該篇文章標題命名的資料夾當中。 <br />
● 透過BeautifulSoup爬取網路資料並解析，結合datetime模組找出當日文章，在使用正則表達式來匹配搜尋結果。 <br />

【外幣轉換試算】
● 輸入yyyy/mm/dd country後，可以透過台灣銀行的匯率來轉換成NTD <br />
● 台灣銀行：https://rate.bot.com.tw/xrt?Lang=zh-TW <br />


【導演電影查詢】
● 模擬在IMDB搜尋導演名字，並將該導演所拍攝之電影以及年份列出 <br />
● IMDB：https://www.imdb.com/ <br />
