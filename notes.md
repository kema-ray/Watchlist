## Template Inheritance
we make use of template inheritance , which allows us to create the part which is same in all webpages => This applies to our navigation bar,footer cos=z they look the same in all the pages.

## Create a flask app to render the main template:
#### Views.py
from flask import Flask
from flask import render_template
## setting up the application
app = Flask(__name__)

## making the route
@app.route('/')
def home():
   return render_template('home.html')

## running the application=>This is done in the run.py file
if __name__ == '__main__':
   app.run(debug=True)

## Create HTML Files
-Create a base.html file in which we have one heading which will be common in all webpages.
## how to download bootstrap=>pip install flask-bootstrap 
   base.html 
    Syntax:
    {% extends 'bootstrap/base.html' %}
    {% block content %}
    {% endblock %}
=>create a home.html file in which we will inherit template from “base.html” file and will write some code for home page also. 
      home.html
      Syntax:
      {% extends "base.html" %}
           {% block content %}
           ##Write code here(<h1>Welcome to Home</h1>)
           {% endblock %}

## Bootstrap=>pip install flask-bootstrap
__init__.py=>
  1.from flask_bootstrap import Bootstrap
  2.bootstrap = Bootstrap(app)

### WTF Forms
-WTF extension which is a flexible form rendering and validation library.
-WTF forms make working with web forms much easier.
-It provides a lot of out of the box functionality 


## Creating blueprints
-A Blueprint is similar to an application in that it can also define routes.
-The main difference is that blueprints are dormant until they are registered by an application.