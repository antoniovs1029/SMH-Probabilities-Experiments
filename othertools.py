import numpy as np

class NipsVocabParser:
    """
    Parses the information in the nips.vocab file (downloaded from knowceans) 
    into np.arrays for frecuencies of words and strings of words.

    For more information, check the README.md
    """
    def __init__(self, vocabfile):
        self.vocabfile = vocabfile

    def get_vocab_frecuencies(self):
        frecuencies = []
        with open(self.vocabfile, 'r') as f:
            for line in f:
                frecuencies.append(line.split(" ")[4])
        return np.array(frecuencies, dtype = int)

    def get_vocab_words(self):
        words = []
        with open(self.vocabfile, 'r') as f:
            for line in f:
                words.append(line.split(" ")[0])
        return words
