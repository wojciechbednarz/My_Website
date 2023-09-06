from flask import Flask
from flask import url_for
from flask import request
from flask import render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/first_page/')
def first_page(name=None):
    return render_template('first_page.html', name=name)


@app.route("/upload", methods=['POST'])
def hello():
    # text = request.form[f"Hello,  {escape(name)}!"]
    text = request.form["text"]
    processed_text = text.upper()
    return render_template('first_page.html', processed_text=processed_text)


with app.test_request_context():
    print(url_for('first_page'))
