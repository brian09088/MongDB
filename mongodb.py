# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pymongo
client = pymongo.MongoClient()
db = client.test

result = db.weather.insert_one({
    'rainy_rate': 60,
    'temperature': 29,
    'date': '2023/6/16 16:01:00'
    })

if  result.acknowledged:
    print(result.inserted_id)
else :
    print('error')
    

#show = db.weather.find()
#print(show)
