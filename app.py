from flask import Flask, render_template

app = Flask(__name__)


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/training")
def training():
    return render_template('coaching.html')


@app.route("/")
def index():
    return render_template('index.html')
