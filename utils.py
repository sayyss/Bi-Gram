# helper functions -> one hot encoding, any vector math
from typing import List
import torch
import torch.nn.functional as F


def one_hot_encode(words: List[str], vocab_size: int) -> List[torch.Tensor]:
    # Create a sorted word-to-index mapping for consistent results
    word_to_index = {word: i for i, word in enumerate(sorted(set(words)))}

    # Convert words to indices
    indices = [word_to_index[word] for word in words]

    # Convert indices to tensor
    indices_tensor = torch.tensor(indices)

    # One-hot encode
    one_hot_vectors = F.one_hot(indices_tensor, num_classes=vocab_size)

    # Return as list of tensors
    return [vec for vec in one_hot_vectors]


# # Example usage
# words = ["apple", "banana", "apple", "cherry"]
# vocab_size = len(set(words))
# one_hot_vectors = one_hot_encode(words, vocab_size)
# for vec in one_hot_vectors:
#     print(vec)
def prepare_data(text_file: str):

    word_list = []

    word = text_file.split()

    for word in word:
        if word not in word_list:
            word_list.append(word)

    vocab_size = len(sorted(list(set(word_list))))

    return vocab_size, word_list


def prepare_input(words, vocab) -> Tuple[List[int]], List[int]]:
    # create a dictionary mapping each word to an index(use get_word_dict func)
    # total indexes: number of unique words in words
    # return pair [x,y]
    # x: word_i, y: word_i+1


# vocab: list of all unique words in the text
def get_word_dict(vocab):

    # Returns two dictionaries, word_to_i, i_to_word
    # word_to_i: map word to an index {"asdas": 1}
    # i_to_word: map index to word {1: "asdas"}
    # return both

