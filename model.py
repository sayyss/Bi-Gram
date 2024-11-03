import torch


class Bigram:

    def __init__(self, vocab):
        self.vocab = vocab
        self.matrix = torch.randn(vocab, vocab)

    def __call__(self, x):
        # placeholder
        logits = self.forward(x)
        return logits

    def forward(self, x):
        # x * matrix
        # return logits(vector)
        logits = torch.matmul(x, matrix)
        return logits

    def generate(self, context, length):
        # given a word, get length amount of words from model and return
        # returns a string

        output = ""
        one_hot_context = one_hot(context)
        for i in range(length):
            next_word = self.forward(one_hot_context)
            index = torch.argmax(next_word)
            output.append(i_to_word[index])
            context = i_to_word[index]


