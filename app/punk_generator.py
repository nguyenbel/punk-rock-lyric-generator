import flask
import numpy as np
import re

import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
from tensorflow import keras

app = flask.Flask(__name__)

model = keras.models.load_model('../models/punk_rock_generator.h5')

with open('../models/lyrics_tokenizer.pkl', 'rb') as f:
    tokenizer_lyrics = pickle.load(f)

with open('../models/artist_tokenizer.pkl', 'rb') as f:
    tokenizer_artist = pickle.load(f)



# define predict function as endpoint
@app.route("/")
def submission_page():
    return flask.render_template('form.html')


@app.route('/predict', methods = ["GET", "POST"])
def predict():
    prompt = str(flask.request.form['lyrics'])
    prompt2 = str(flask.request.form['lyrics'])
    author = str(flask.request.form['artists'])
    length = int(flask.request.form['length'])
    vocab_size = 5979
    # edge case; if prompt is as long as the length wanted
    if len(prompt.split(' ')) == length:
        return f'"{prompt}" in the style of "{author}:"           {prompt2}'

    else:
        a = [re.sub(r'\W', '', string = author)]
        
        a = np.array(tokenizer_artist.texts_to_sequences(a))
        
        for _ in range(20 - len(prompt.split(' '))):

            token_list = tokenizer_lyrics.texts_to_sequences([prompt])[0]
            token_padded = pad_sequences([token_list], maxlen = 10)

            # get predicted probability for each word
            predicted_probs = model.predict([token_padded, a])[0]

            # using temperature for next word
            probabilities = np.exp(predicted_probs / 1)
            normalized_probablities = probabilities / sum(probabilities)
            next_word = np.random.choice(range(vocab_size), p=normalized_probablities)
            next_word = tokenizer_lyrics.index_word[next_word]


            # add word to the prompt
            if len(next_word) > 1 and (next_word != 'a' or next_word != 'i'):
                prompt2 += ' ' + str(next_word)
        return f'"{prompt}" in the style of "{author}:"           {prompt2}'



if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080, debug = True)