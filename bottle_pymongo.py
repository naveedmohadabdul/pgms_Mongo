import bottle
import pymongo

@bottle.route('/')
def index():
	connection  = pymongo.MongoClient('localhost',27017)
	db = connection.test
	naveed = db.naveed
	item = naveed.find()
	item = item[1]
	return '</b>Hello %s!</b>' % item['father']

bottle.run(host='localhost',port=8802)

