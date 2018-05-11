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
    print(text)
    processed_text = write_top_results_to_string(text)
    return processed_text.replace("\n", "<br/>")

#SEMINAR
@app.route('/tag', methods=['POST', 'GET'])
def tag_post_sem():
    tag ='seminar'
    print(tag)
    processed_text = write_events_by_tag_to_string(tag)
    return processed_text.replace("\n", "<br/>")

#LECTURE
@app.route('/tag1', methods=['POST'])
def tag_post_lect():
    tag ='lecture'
    print(tag)
    processed_text = write_events_by_tag_to_string(tag)
    return processed_text.replace("\n", "<br/>")

#MEETING
@app.route('/tag2', methods=['POST', 'GET'])
def tag_post_meet():
    tag ='meeting'
    print(tag)
    processed_text = write_events_by_tag_to_string(tag)
    return processed_text.replace("\n", "<br/>")

#EXHIBITION
@app.route('/tag3', methods=['POST', 'GET'])
def tag_post_ex():
    tag ='exhibition'
    print(tag)
    processed_text = write_events_by_tag_to_string(tag)
    return processed_text.replace("\n", "<br/>")

#CONFERENCE
@app.route('/tag4', methods=['POST', 'GET'])
def tag_post_conf():
    tag ='conference'
    print(tag)
    processed_text = write_events_by_tag_to_string(tag)
    return processed_text.replace("\n", "<br/>")

#WORKSHOP
@app.route('/tag5', methods=['POST', 'GET'])
def tag_post_work():
    tag ='workshop'
    print(tag)
    processed_text = write_events_by_tag_to_string(tag)
    return processed_text.replace("\n", "<br/>")

#OTHER
@app.route('/tag6', methods=['POST', 'GET'])
def tag_post_oth():
    tag ='other'
    print(tag)
    processed_text = write_events_by_tag_to_string(tag)
    return processed_text.replace("\n", "<br/>")



if __name__ == '__main__':
    app.run(debug=True)
