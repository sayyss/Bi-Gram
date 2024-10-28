# helper functions -> one hot encoding, any vector math

def one_hot_encode(words: List[str], vocab: int) -> List[float]:

def prepare_data(text_file: str):

    word_list = []

    word = text_file.split()

    for word in word:
        if word not in word_list:
            word_list.append(word)
    
    vocab_size = len(word_list)

    return vocab_size, word_list


def prepare_input(words, vocab) -> Tuple[List[int], List[int]]:


