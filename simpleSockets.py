from flask import Flask, render_template, redirect
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


	#load display page
	return render_template("testDisplay.html")

@sockets.route('/crawl')
def startCrawl(ws):

	#fakeCrawler.crawl(ws)
	crawler.crawl(ws, "http://www.apple.com", 6, "dfs", "keyword")

if __name__ == "__main__":
	app.run()

#gunicorn simpleSockets:app --workers 2 --error-logfile - --reload

