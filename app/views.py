from flask import render_template
from app import app
from flask import request





@app.route('/')
def index():
	#anything in the return statement gets sent to the browser
	#e.g you can open a html file and send that
	return "Hello Kevin"

@app.route('/about')
def about():
	
	#you use these functions and the app.route decorators
	#to specify what will be returned for each link
	#It gets a bit more complicated. E.g the @app.routes can accept variables

	#But that's pretty much it

	#Suggest you look at flask requests, jinja templates, and connecting to a database
	return "This is all you need to get started with flask"

