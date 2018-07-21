from flask import Flask, render_template
from flask_sockets import Sockets
import os
import fakeCrawler
import time

app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/')
def index():
    return render_template('testIndex.html')

@app.route('/testSubmit', methods=['POST'])
def launch():

	#launch fake crawler
	if not os.fork():
		fakeCrawler.crawl()

	#load display page
	return render_template("testDisplay.html")

if __name__ == "__main__":
	app.run()

#gunicorn simpleSockets:app --workers 2 --error-logfile - --reload

