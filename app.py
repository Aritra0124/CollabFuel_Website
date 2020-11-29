from flask import Flask, render_template, json

app = Flask(__name__)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('topic.html', c_name="Page Not Found", image_name="notfound.png", topic=[])


def module_data(module):
    module_list = json.loads(open("data", "r").read())
    return module_list[module]


@app.route("/topic/<topic_name>")
def topic(topic_name):
    if topic_name == "contact":
        return render_template('topic.html', c_name="Contact Us")
    else:
        topic_data = module_data(topic_name)
        return render_template('topic.html', c_name=topic_data["name"], image_name=topic_data["image"],
                               topics=topic_data["topic"])


@app.route("/")
def index():
    return render_template('index.html')
