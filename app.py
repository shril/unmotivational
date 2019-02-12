from flask import Flask
from waitress import serve
import requests
import random

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_quote():
	r = requests.get('https://api.sheety.co/807cbee0-6212-45be-8e51-868d9f81ae53')
	quotes = r.json()
	return random.choice(quotes)['quotes']

if __name__ == '__main__':
	serve(app, host='0.0.0.0', port=5000)