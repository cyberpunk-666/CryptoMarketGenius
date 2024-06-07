import base64
import configparser
import hashlib
import hmac
import time
from urllib.parse import quote as url_quote
from flask import Flask, jsonify, render_template
import requests
import urllib3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/markets')
def markets():
    return render_template('markets.html')

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/tools')
def tools():
    return render_template('tools.html')

@app.route('/community')
def community():
    return render_template('community.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Load API credentials from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

API_KEY = config['kraken']['API_KEY']
API_SECRET = config['kraken']['API_SECRET']

def kraken_request(uri_path, data):
    url = f"https://api.kraken.com{uri_path}"
    nonce = str(int(time.time() * 1000))
    data['nonce'] = nonce
    postdata = urllib3.parse.urlencode(data)
    encoded = (str(data['nonce']) + postdata).encode()
    message = uri_path.encode() + hashlib.sha256(encoded).digest()
    signature = hmac.new(base64.b64decode(API_SECRET), message, hashlib.sha512)
    headers = {
        'API-Key': API_KEY,
        'API-Sign': base64.b64encode(signature.digest()).decode()
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()

@app.route('/kraken/balance', methods=['GET'])
def get_balance():
    data = {
        'nonce': str(int(time.time() * 1000)),
    }
    balance = kraken_request('/0/private/Balance', data)
    return jsonify(balance)

if __name__ == '__main__':
    app.run(debug=True)
