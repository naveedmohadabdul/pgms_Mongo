import bottle
import pymongo

@bottle.route('/')
def home_page():
	return 'Hello World\n'

@bottle.route('/testpage')
def test_page():
	return "This is a Test Page\n\n"

bottle.debug(True);
bottle.run(host='localhost',port=8080)
