from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

#   from src.app import app

@app.route('/')
def home():
    """Renders a Home page."""
	# Testing 123 Fuck Face
    return "Hello"
 
if __name__=="__main__":
  app.run(debug=True)
