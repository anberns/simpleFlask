from flask import Flask, render_template, redirect
from flask_sockets import Sockets
import os
import fakeCrawler
import time

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
	while True:
		time.sleep(1)
		#ws.send("Hello world")
		fakeCrawler.crawl(ws)

if __name__ == "__main__":
	app.run()

#gunicorn simpleSockets:app --workers 2 --error-logfile - --reload

