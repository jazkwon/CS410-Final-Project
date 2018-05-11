from flask import Flask, render_template, request
from functools import wraps
import json
from pprint import pprint
from Search import *

app = Flask(__name__, static_url_path = "", static_folder = "static")

@app.route('/')
def search():
    return render_template('index.html')

@app.route('/generate')
def generate():
	#load the file
	#call a function that parses the file
	return render_template('test3.html')

@app.route('/', methods=['POST'])
def search_post():
    text = request.form['text']
    processed_text = write_top_results_to_string(text)
    return processed_text

if __name__ == '__main__':
    app.run(debug=True)
