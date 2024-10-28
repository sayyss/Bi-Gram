# helper functions -> one hot encoding, any vector math

def one_hot_encode(words: List[int], vocab: int) -> List[float]:
    # uses pytorch's one_hot function to create one hot vectors of class size: vocab

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

