import numpy as np


def nips_get_vocab_frecuencies(vocabfile):
    frecuencies = []
    with open(vocabfile, 'r') as f:
        for line in f:
            frecuencies.append(line.split(" ")[4])
    return np.array(frecuencies, dtype = int)

def nips_get_vocab_words(vocabfile):
    words = []
    with open(vocabfile, 'r') as f:
        for line in f:
            words.append(line.split(" ")[0])
    return words
