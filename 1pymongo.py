import pymongo 

from pymongo import MongoClient


connection = MongoClient('localhost',27017)

db = connection.test

naveed = db.naveed

item = naveed.find()
item = item[1]
print item['father']

try:
 print item['Mother'] 
except Exception:
 print item['mother']

