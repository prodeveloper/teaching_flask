from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask import make_response
from flask import request

import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/save", methods=['POST'])
def save():
    response = make_response(redirect(url_for('index')))
    response.set_cookie('character', json.dumps(dict(request.form.items())))
    return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
