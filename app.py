from urllib.parse import quote as url_quote
from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run(debug=True)
