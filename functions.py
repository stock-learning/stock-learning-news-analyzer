from keras.datasets import imdb
from keras.preprocessing import sequence
from setting import get_env

num_values = int(get_env('NUM_VALUES'))

def load_trainig_data():
    global num_values
    (train_data, train_labels), (test_data, test_labels) = imdb.load_data(num_words=num_values)
    return train_data, train_labels, test_data, test_labels

def format_sequence_elements(data, words, _padding='post', _maxlen=256):
    return sequence.pad_sequences(data, value=words['<PAD>'], padding=_padding, maxlen=_maxlen)

# A dictionary mapping words to an integer index
# The first indices are reserved
def get_word_settings():
    _word_index = imdb.get_word_index()
    _word_index = {k:(v+3) for k,v in _word_index.items()} 
    _word_index['<PAD>'] = 0
    _word_index['<START>'] = 1
    _word_index['<UNK>'] = 2  # unknown
    _word_index['<UNUSED>'] = 3
    return _word_index

def get_num_values():
    global num_values
    return num_values

def splitting(data, labels):
    global num_values
    return data[num_values:], labels[num_values:], data[:num_values], labels[:num_values]