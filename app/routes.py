from flask import render_template, url_for, request
from app import app
from src.utils import utils

@app.route('/')
def index():
    return render_template('greetings.html')

@app.route('/get_greeting', methods=['GET', 'POST'])
def get_greeting():
    if request.method == 'POST':
        image = request.form.get('image')
        name = request.form.get('name')
        relation = request.form.get('relation')
        context = request.form.get('context')

        return render_template('greetings.html')
    
    return render_template('greetings.html')
