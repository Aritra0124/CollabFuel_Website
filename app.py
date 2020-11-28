from flask import Flask, render_template

app = Flask(__name__)

@app.route("/coaching")
def training():
    return render_template('coaching.html')




@app.route("/")
def index():
    return render_template('index.html')
