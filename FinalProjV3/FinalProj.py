from datetime import datetime
from flask import render_template, request, make_response, Response
from flask import Flask
# from mcqgeneration import *
# from nounfiltering import *


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def go_to_home():
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )


@app.route('/mcqgen', methods=["GET", "POST"])
def mcq_generation():
    # content = request.form["text"]
    return render_template(
        'mcqGeneration.html'
    )


if __name__ == '__main__':
    app.run(port=50000, debug=True)
