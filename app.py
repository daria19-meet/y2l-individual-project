from flask import Flask, render_template, url_for
from database import * 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<dancer_name>', methods=["GET"])
def dancer_page(dancer_name):
	dancer=query_dancer_by_name(dancer_name)
	return render_template('dancer.html', dancer=dancer)

@app.route('/<dance_style>', methods=["GET"])
def dance_page(dance_style):
	style=query_dance_by_name(dance_style)
	dancers=query_dancer_by_style(dance_style)
	return render_template('dance_style.html', style=style, dancers=dancers)

if __name__ == '__main__':
    app.run(debug=True)

