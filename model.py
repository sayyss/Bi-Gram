import torch
from utils import *

class Bigram:

    def __init__(self, vocab):
        self.vocab = vocab
        self.matrix = torch.randn(len(self.vocab), len(self.vocab))
        self.parameters = [self.matrix]
        self.softmax = torch.nn.Softmax(dim=1)

        for i in self.parameters:
            i.requires_grad = True

    def __call__(self, x):
        # placeholder
        logits = self.forward(x)
        return logits

    def forward(self, x):
        # x * matrix
        # return logits(vector)
        logits = torch.matmul(x, self.matrix)
        return logits

    def generate(self, context, length, word_to_i, i_to_word):
        # given a word, get length amount of words from model and return
        # returns  

        output = []
        for i in range(length):
            context = torch.tensor([word_to_i[context]])
            context = one_hot_encode(context, len(self.vocab))
            next_word = self.forward(context)
            index = torch.argmax(self.softmax(next_word))
            output.append(i_to_word[index.item()])
            context = i_to_word[index.item()]


        return ' '.join(output)


