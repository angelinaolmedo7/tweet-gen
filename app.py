from flask import Flask
from word_freq import weighted_sample, weighted_phrase

app = Flask(__name__)


@app.route('/')
def hello_world():
    return weighted_phrase("simpleHist.txt")
