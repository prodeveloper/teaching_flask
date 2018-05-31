from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/save", methods=['POST'])
def save():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
