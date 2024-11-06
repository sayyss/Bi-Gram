
from utils import * 

def train(text_file):

    # prepare vocab
    # create model
    # train model
    # return model

    words, vocab = prepare_data(text_file)

    words_to_i, i_to_words = get_word_dict(vocab)
    x,y = prepare_input(words, words_to_i)

    print(len(vocab))
    print(x[:10])
    print(y[:10])
train("random_input.txt")

