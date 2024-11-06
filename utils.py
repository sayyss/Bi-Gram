# helper functions -> one hot encoding, any vector math
from typing import List
import torch
import torch.nn.functional as F
import re

def one_hot_encode(words, vocab_size):
    one_hot_vectors = F.one_hot(words, num_classes=vocab_size)

    # Return as list of tensors
    return [vec for vec in one_hot_vectors]


# # Example usage
# words = ["apple", "banana", "apple", "cherry"]
# vocab_size = len(set(words))
# one_hot_vectors = one_hot_encode(words, vocab_size)
# for vec in one_hot_vectors:
#     print(vec)
def prepare_data(text_file: str):

    file_content = open(text_file, "r").read()
    file_content = file_content.lower()
    file_content = re.sub(r'[^a-zA-Z\s]', '', file_content)
    file_content = file_content.split()

    # all unique words in file
    vocab = sorted(list(set(file_content)))

    return file_content, vocab


def prepare_input(words, words_to_i):

    # x[0], y[0] = word[i], word[i+1]
    x = words[:-1]
    y = words[1:]

    # use indexes
    x = [words_to_i[word] for word in x]
    y = [words_to_i[word] for word in y]
    
    return x, y


def get_word_dict(vocab):
    
    words_to_i = {}
    i_to_words = {}
    
    for i in enumerate(vocab):
        #('word', index) <=> (index, 'word')
        words_to_i[i[1]] = i[0]
        i_to_words[i[0]] = i[1]
        
    return words_to_i, i_to_words
