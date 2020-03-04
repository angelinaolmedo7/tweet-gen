from flask import Flask, render_template, request, redirect, url_for
from markov import MarkovChain
from usernameGenerator import get_username

app = Flask(__name__)


taz_chain = MarkovChain(MarkovChain.read_text_file("taz_murderOnTheRockportLimited.txt"))


@app.route('/')
def index():
    """Return homepage."""
    tweets = []
    for i in range(0, 12):
        tweet = {
            "user": get_username(),
            "content": taz_chain.walk(12)
        }
        tweets.append(tweet)
    return render_template('home.html', tweets=tweets)


@app.route('/about')
def about():
    """Return the about page."""
    return render_template('about.html')
