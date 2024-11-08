
from utils import * 
import torch
from model import Bigram


def train(text_file):

    # prepare vocab
    # create model
    # train model
    # return model

    words, vocab = prepare_data(text_file)

    words_to_i, i_to_words = get_word_dict(vocab)
    x,y = prepare_input(words, words_to_i)
    vocab_size = len(vocab)

    print(vocab_size)

    x = torch.tensor(x)
    y = torch.tensor(y)

    x = one_hot_encode(x, vocab_size)
    y = one_hot_encode(y, vocab_size)

    epochs = 50
    model = Bigram(vocab)
    CEL = torch.nn.CrossEntropyLoss()
    lr = 0.01
    optimizer = torch.optim.SGD(model.parameters, lr, momentum=0.9)

    for i in range(epochs):
        logits = model(x)
        loss = CEL(logits, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()


    print(model.generate("there", 10, words_to_i, i_to_words))

    return model


model = train("random_input.txt")
