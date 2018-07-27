from flask import Flask, render_template, request
from flask_sockets import Sockets
import os
import fakeCrawler
import crawler
import time
import random

app = Flask(__name__)
app.config.from_pyfile('config.py')
sockets = Sockets(app)

@app.route('/')
def index():
    return render_template('testIndex.html')

@app.route('/testSubmit', methods=['POST'])
def launch():
	global userId, url, limit, sType, keyword
	url = "https://" + request.form['url']
	limit = request.form['limit']
	sType = request.form['type']
	keyword = request.form['keyword']

	#load display page
	return render_template("testDisplay.html")

@sockets.route('/crawl')
def startCrawl(ws):

	#fakeCrawler.crawl(ws)
	global userId, url, limit, sType, keyword
	crawler.crawl(ws, url, int(limit), sType, keyword)
if __name__ == "__main__":
	app.run()

#gunicorn simpleSockets:app --workers 2 --error-logfile - --reload

