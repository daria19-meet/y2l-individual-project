from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<dancer_name>', methods=["GET"])
def dancer(name):
	dancer=query_dancer_by_name(name)
	return render_template('dancer.html', dancer=dancer)


if __name__ == '__main__':
    app.run(debug=True)

