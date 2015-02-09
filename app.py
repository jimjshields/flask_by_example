from flask import Flask
import os

app = Flask(__name__)

if os.environ.get('APP_SETTINGS', '') == '':
	app.config.from_object('config')
else:
	app.config.from_object(os.environ.get('APP_SETTINGS', ''))
	

@app.route('/')
def index():
	return 'Hello world!'

@app.route('/<name>')
def hello_name(name):
	return 'Hello {}!'.format(name)

if __name__ == '__main__':
	app.run()