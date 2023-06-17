# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 13:24:07 2023

@author: User
"""
import pymongo
from pprint import *

client = pymongo.MongoClient()
db = client.opendata

for document in db.AQI.find():
    print('{County}{SiteName}: {AQI}'.format(**document))

#查詢第一筆資料
first = db.AQI.find()[0]
print('{SiteName}: {AQI}'.format(**first))

#取得最後三筆資料
for last_three in list( db.AQI.find() )[-3:]:
    print('{SiteName}: {AQI}'.format(**last_three))
    
#查詢特定欄位，boolean:1代表要顯示欄位
cursor = db.AQI.find({}, {'County': 1,'SiteName' : 1, '_id': 0})
pprint(list(cursor))

#單一/多重條件查詢
a1 = db.AQI.find({'County': '澎湖縣'})
pprint(list(a1))

a2 = db.AQI.find({
    '$or' : [
            {'SiteName': '淡水'},
            {'SiteName': '板橋'}
            ]
    })
pprint(list(a2))