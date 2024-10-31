# helper functions -> one hot encoding, any vector math
from typing import List, Tuple, Dict
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


def prepare_data(text_file: str):

    word_list = []

    word = text_file.split()

    for word in word:
        if word not in word_list:
            word_list.append(word)

    vocab_size = len(sorted(list(set(word_list))))

    return vocab_size, word_list


# vocab: list of all unique words in the text
# Returns two dictionaries, word_to_i, i_to_word
# word_to_i: map word to an index {"asdas": 1}
# i_to_word: map index to word {1: "asdas"}
# return both
def get_word_dict(vocab: List[str]) -> Tuple[Dict[str, int], Dict[int, str]]:
    # Create dictionaries to map words to indices and indices to words
    word_to_indices = {word: idx for idx, word in enumerate(vocab)}
    indices_to_word = {idx: word for idx, word in enumerate(vocab)}
    return word_to_indices, indices_to_word


# create a dictionary mapping each word to an index(use get_word_dict func)
# total indexes: number of unique words in words
# return pair [x,y]
# x: word_i, y: word_i+1
# Get the word to index and index to word dictionaries
def prepare_input(words: List[str], vocab: List[str]) -> Tuple[List[int], List[int]]:
    # Get the word to index and index to word dictionaries
    word_to_index, _ = get_word_dict(vocab)

    # Map each word in the input list to its corresponding index
    indices = [word_to_index[word] for word in words if word in word_to_index]

    # Prepare pairs (x, y) where x is word_i and y is word_i+1
    x = indices[:-1]
    y = indices[1:]

    return x, y




