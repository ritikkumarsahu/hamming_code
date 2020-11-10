from flask.templating import render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/visualize')
def visualize():
    return render_template('visualize.html')