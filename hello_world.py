import bottle

@bottle.route('/')
def home_page():
	mythings = ['apple','orange','peach']
	return bottle.template('hello_world',username='Naveed',things=mythings)
#	return bottle.template('hello_world',{'username':'Rohit','things':'mythings'})

@bottle.post('/favorite_fruit')
def favorite_fruit():
	fruit = bottle.request.forms.get("fruit")
	if(fruit==None or fruit==""):
		fruit = "No Fruit Selected"
	
	return bottle.template('fruit_selection.tpl',{'fruit':fruit})


bottle.debug(True)
bottle.run(host='localhost',port=8080)
