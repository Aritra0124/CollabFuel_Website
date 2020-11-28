from flask import Flask, render_template

app = Flask(__name__)


def module_data(module):
    image_file = {"aws": "aws.png", "terraform": "terraform.png", "selenium": "selenium.png", "python": "py.png",
                  "kubernates": "kubernates.png", "ai": "ai.png", "security": "cour1.png"}
    return image_file[module]


@app.route("/topic/<topic_name>")
def topic(topic_name):
    topics = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    image_name = module_data(topic_name)
    return render_template('topic.html', c_name=topic_name, topics=topics, image_name=image_name)


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/training")
def training():
    return render_template('training.html')


@app.route("/")
def index():
    return render_template('index.html')
