# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 15:02:26 2022

@author: Neal
shareholder information of a stock are listed in :
https://q.stock.sohu.com/cn/000001/ltgd.shtml
https://q.stock.sohu.com/cn/000002/ltgd.shtml
https://q.stock.sohu.com/cn/000003/ltgd.shtml
...

And you are requried to collect the tables of shareholder information for stocks in "select_stocks"
with following 7 columns, and then perform the analysis to answer the questions.
    1. 'stock'-股票代码
    2. 'rank'-排名
    3. 'org_name'-股东名称	
    4. 'shares'-持股数量(万股)
    5. 'percentage'-持股比例	
    6. 'changes'-持股变化(万股)
    7. 'nature'-股本性质
    
Please pay attention to the data types of different columns, especially 'rank', 'percentage'
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import numpy as np
fake_header = {  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
            "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate, sdch",
            "Accept-Language":"zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4,zh-CN;q=0.2"
        }

data_file= './data/stock_shareholders.csv'
select_stocks = ('600905','600958','601186','600029','600111','601857','601818','600048',
             '601800','601788','601766','601688','601668','601628','601601')



print('There are',len(select_stocks), 'stocks in select_stocks')

base_url = 'https://q.stock.sohu.com/cn/{}/ltgd.shtml' 
row_count = 0
#create a list to store the crawled share-holdoing records
results=[]
for stock in select_stocks:#process stock one by one
    #prepare the request webpage with desired parameters
    url = base_url.format(stock)
    print("Now we are crawling stock",stock)
    #send http request with fake http header
    response = requests.get(url,headers = fake_header)
    if response.status_code == 200:
        #++insert your code here++ to set the encoding of response according to the charset of html
        response.encoding = 'gb2312'
        root = BeautifulSoup(response.text,"html.parser") 
        # search the table storing the shareholder information
        table = root.find(class_='tableG')
        # list all rows the table, i.e., tr tags
        rows =  table.find_all("tr")[1:]#++insert your code here++
        for row in rows: #iterate rows
            record=[stock,]# define a record with stock pre-filled and then store columns of the row/record
            # list all columns of the row , i.e., td tags
            columns = row.find_all("td") #++insert your code here++
            for col in columns: #iterate colums
                record.append(col.get_text().strip())
                #print(record)
            if len(record) == 7:# if has valid columns, save the record to list results
                #++insert your code here++ to add single "record" to list of "records"
                results.append(record)
                row_count+=1
        time.sleep(1)
print('Crawled and saved {} records of shareholder information of select_stocks to{}'.format(row_count,data_file) )

sharehold_records_df = pd.DataFrame(columns=['stock', 'rank','org_name','shares','percentage','changes','nature'], data=results)
sharehold_records_df.to_excel("./data/sharehold_records.xlsx")
print("List of shareholers are \n", sharehold_records_df['org_name'])

#insert your code here to answer Q3-1, Q3-2 and Q3-3
#Q3-1

mydata = pd.DataFrame(results)
mydata.columns = ['stock', 'rank','org_name','shares','percentage','changes','nature']

f = lambda x: int(x)<=3
mydata_1=mydata[mydata["rank"].apply(f)]
print("Q1-1")
mydata_1["org_name"]
orgs = np.unique(mydata_1["org_name"])
for org in orgs:
    print(org)
print('There are {} unique organizations that are among the top 3 (rank<=3) shareholders of any stocks in  select_stocks'.format(len(orgs)))
print("*"*50)
#Q3-2
#使用collections模块下的Counter类
from collections import Counter
list=mydata["org_name"]
result=Counter(list)
result=dict(result)
d_tmp = dict((key, value) for key, value in result.items() if float(value) >= 3)
print("Q1-2")
print(d_tmp)
print(len(d_tmp))
print("*"*50)
#Q3-3
f = lambda x: float(x.strip("%"))
mydata["percentage"] = mydata["percentage"].apply(f)
mygroup = mydata.groupby("org_name").agg({"percentage":"sum"}).sort_values(by = "percentage",ascending = False)
print("Q1-3")
print(mygroup.iloc[1,])
