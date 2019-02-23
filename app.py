from flask import Flask, request
from flask_cors import CORS, cross_origin
import requests
import random
from waitress import serve

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
requests_cache.install_cache('sheetly_cache', backend='sqlite', expire_after=600)

print ('App Loaded')
app.logger.info('Info')
# print (quotes)

@app.route('/')
@cross_origin()
def get_quote():
	if request.method == 'GET':
		quotes = requests.get('https://api.sheety.co/807cbee0-6212-45be-8e51-868d9f81ae53').json()
		print (request.remote_addr)
		print (request.environ['REMOTE_ADDR'])
		print ()
		result = random.choice(quotes)['quotes']
		print (result)
		return result

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=80)
app.py (END)