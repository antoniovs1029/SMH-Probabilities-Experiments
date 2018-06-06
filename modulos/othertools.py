import numpy as np


def nips_get_vocab_frecuencies(vocabfile):
    """
    Convert the nips.vocab file into an array of frecuencies
    where the i-th element of the array is the frecuency of the
    word with index i.

    :param vocabfile: string, path to the nips.vocab file
    :return numpy array with frecuencies
    """
    frecuencies = []
    with open(vocabfile, 'r') as f:
        for line in f:
            frecuencies.append(line.split(" ")[4])
    return np.array(frecuencies, dtype = int)

def nips_get_vocab_words(vocabfile):
    """
    Convert the nips.vocab file into a list of strings
    where the string in the i-th position is the string of
    the word with index i

    :param vocabfile: string, path to the nips.vocab file
    :return list of words
    """
    words = []
    with open(vocabfile, 'r') as f:
        for line in f:
            words.append(line.split(" ")[0])
    return words
