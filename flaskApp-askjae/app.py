from flask import Flask, render_template
from functools import wraps
import json
from pprint import pprint

app = Flask(__name__, static_folder = "tmp")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate():
	#load the file
	#call a function that parses the file
	return render_template('test3.html')

if __name__ == '__main__':
    app.run(debug=True)

