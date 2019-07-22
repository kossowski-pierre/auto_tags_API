from flask import Flask, url_for, render_template, request
from .utils import get_tags
import pandas as pd
#import pandas as pd

app=Flask(__name__)

@app.route('/')
@app.route('/index/')
def index():
	return render_template('index.html')

@app.route('/result/')
def result():
	title=request.args.get('title')
	post=request.args.get('post')
	text= title + ' ' + post

	result=get_tags(text=text)
	if text == ' ':
		result = "No question -> No tag"

	return render_template('result.html', result=result)
