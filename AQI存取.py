# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 09:01:38 2023

@author: User
"""
import urllib.request as urllib
import json
import pymongo

#api_key = '9be7b239-557b-4c10-9775-78cadfc555e9'

url = 'https://raw.githubusercontent.com/kirkchu/mongodb/main/aqi.json'

#api_key + '&format=json'

response = urllib.urlopen(url)
text = response.read().decode('utf-8')

#print(text)

text = text.replace('"AQI": ""', '"AQI": "-1"')
jsonObj = json.loads(text)

client = pymongo.MongoClient()
    
#請注意，不是client.opendata()
db = client["opendata"]

'''
執行後自動新增資料庫與資料表，不需要手動設定
'''
db.AQI.insert_many(jsonObj['records'])
