from flask import Flask, render_template, request, session
from flask_sockets import Sockets
import os
import fakeCrawler
import crawler
import time
import random

app = Flask(__name__)
app.secret_key = os.urandom(24)
sockets = Sockets(app)

@app.route('/')
def index():
    return render_template('testIndex.html')

@app.route('/testSubmit', methods=['POST'])
def launch():
	global userId, url, limit, sType, keyword
	url = "https://www.nytimes.com" #"https://" + request.form['url']
	limit = 4 #request.form['limit']
	sType = "dfs" #request.form['type']
	keyword = None #request.form['keyword']
	session['url'] = url
	session['limit'] = limit
	session['sType'] = sType
	session['keyword'] = keyword

	#load display page
	return render_template("testDisplay.html")

@sockets.route('/crawl')
def startCrawl(ws):

	#fakeCrawler.crawl(ws)
	global userId, url, limit, sType, keyword
	url = "https://www.nytimes.com" #"https://" + request.form['url']
	limit = 4 #request.form['limit']
	sType = "dfs" #request.form['type']
	keyword = None #request.form['keyword']
	crawler.crawl(ws, url, int(limit), sType, keyword)
if __name__ == "__main__":
	app.run()

#gunicorn simpleSockets:app --workers 2 --error-logfile - --reload

