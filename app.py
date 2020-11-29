from flask import Flask, render_template, json

app = Flask(__name__)


@app.errorhandler(404)
def not_found_error(error):
    return render_template('topic.html', c_name="Page Not Found", image_name="notfound.png", topic=[])


@app.errorhandler(500)
def found_but_error(error):
    return render_template('topic.html', c_name="Error at displaying", image_name="notfound.png", topic=[])


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
    about = "CollabFuel is the number one software training service provider for the students and professionals " \
            "desiring to make a career in the Information Technology, Financial Technology, E-Commerce, " \
            "and Data Analysis domain.The syllabus designed under the mentorship of IIT/IIM alumni, enables our " \
            "students to respond to the upcoming job market, which has been marked with developments like Artificial " \
            "Intelligence, Machine Learning, Edge and Cloud Computing, Block Chain, Quantum Computing, " \
            "and Cyber Security.Our trainers are industry veterans, who bring their knowledge of real-life business " \
            "scenarios with adaptive pedagogy, so as to upgrade the student’s skillset at par with the industry " \
            "requirements. This has enabled our students to work with leading organizations like Amazon, Facebook, " \
            "Microsoft, Paytm, TCS, Accenture, Infy. "
    return render_template('index.html',  about=about)
