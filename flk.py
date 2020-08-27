from flask import Flask, session, redirect, url_for, request
from flask import render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('Form.html')


"""
@app.route('/<string:name>')
def hello(name):
	return f"Hello, {name}"
"""

@app.route('/index')
def index():
	headline="Your mama"
	return  render_template("index.html", headline="headline")



if __name__ == '__main__':
    app.run(debug=True)