import torch


class Bigram:

    def __init__(self, vocab):
        self.vocab = vocab
        self.matrix = torch.randn(vocab, vocab)

    def __call__(self, x):
        # placeholder

    def forward(self, x):
        # x * matrix
        # return logits(vector)

    def generate(self, context, length):
        # given a word, get length amount of words from model and return
        # returns a string
