from flask.templating import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/visualise')
def visualise():
    return render_template('visualise.html')