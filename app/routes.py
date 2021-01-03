from flask import render_template, url_for, request
from werkzeug.utils import secure_filename
import os

from app import app
from src.utils import utils
import io

@app.route('/')
def index():
    return render_template('greetings.html')

@app.route('/get_greeting', methods=['GET', 'POST'])
def get_greeting():
    if request.method == 'POST':
        image = request.files['image']
        name = request.form.get('name')
        relation = request.form.get('relation')
        context = request.form.get('context')
        image.save(os.path.join('data/images', image.filename))

        greeting = utils.generate_greeting(name, relation, context, image.filename)
        
        # #Passing image
        # with io.open(os.path.join('data/images', image), 'rb') as image_file:
        #     content = image_file.read()

        # image = vision.Image(content=content)

        return render_template('generated_greeting.html', greeting = greeting)
    
    return render_template('greetings.html')
