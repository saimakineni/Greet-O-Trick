from google.cloud import vision
from src.similarity import similarity
import io
import os

def call_google_api(image_name):
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # Loads the image into memory
    with io.open(os.path.join('data/images', image_name), 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    #Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations
    return labels

def generate_greeting(name, relation, context, image_name):
    labels = call_google_api(image_name)
    keywords = [label.description for label in labels]
    keywords.extend([name, relation, context])
    greeting = similarity.get_high_score_text(keywords, 'data/greetings_newyear.pickle')

    return greeting