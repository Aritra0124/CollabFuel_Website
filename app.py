from flask import Flask, render_template, json

app = Flask(__name__)


def module_data(module):
    module_list = json.loads(open("data", "r").read())
    return module_list[module]


@app.route("/topic/<topic_name>")
def topic(topic_name):
    topic_data= module_data(topic_name)
    return render_template('topic.html', c_name=topic_data["name"], image_name = topic_data["image"], topics = topic_data["topic"])


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/training")
def training():
    return render_template('training.html')


@app.route("/")
def index():
    return render_template('index.html')
