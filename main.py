from flask import Flask
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)


@app.route('/first_page/')
def first_page(name=None):
    return render_template('first_page.html', name=name)


with app.test_request_context():
    print(url_for('first_page'))