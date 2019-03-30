from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import pickle
import numpy as np

def predict(text):

    model = load_model('models/saved.h5')

    with open('models/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    twt = [text]
    twt = tokenizer.texts_to_sequences(twt)
    twt = pad_sequences(twt, maxlen=28, dtype='int32', value=0)
    sentiment = model.predict(twt,batch_size=1,verbose = 2)[0]

    return int(np.argmax(sentiment))
