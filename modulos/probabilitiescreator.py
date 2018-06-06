#!/usr/bin/env python
# Antonio Velazquez
# 2018
# Written in Python 3.5+

"""
Implements different methods to create probabilities distributions
of words over topics, after having used the SMH tool to mine the
topics. (See README.md for more information).
"""

import numpy as np

class Method1:
    """
    Assigns probabilities by assuming that all the occurrences of a word belong
    to the topic; even if the word appears in different topics. An prints a file
    with the calculated probabilities.

    Thus, the probability that word 'w' appears given topic 't' is:
    p(w|t) = 
        (# of ocurrences of word 'w' in the corpus) /
        (sum of all occurrences of every word in topic 't')

    """
    def __init__(self, topicsfile, vocab_frecs, outputfile = 'method1.probs'):
        """
        Construct a new Method1 object
        
        :param topicsfile: file where every line 'n' is the set of the ids of
        the words that belong to topic 'n'

        :param vocab_frecs: numpy array where element 'i' is the frecuency of
        word 'i' in the corpus

        :param outputfile: string path of the text file where the probabilities
        are going to be assigned 

        :return: returns nothing
        """
        self.topicsfile = topicsfile
        self.vocab_frecs = vocab_frecs
        self.outputfile = outputfile

    def run(self):
        """
        Runs the method1 to create the file containing the probabilities assignations
        :return: returns nothing
        """
        with open(self.outputfile, 'w') as f:
            pass # Para borrar el archivo en caso de que exista
        # TODO: Ver otra manera de crear archivos, y borrarlos en caso de que existan

        with open(self.topicsfile, 'r') as f:
            for topic in f: # every line is a topic
                words_ids = np.array([int(x.split(":")[0]) for x in \
                                                topic.split(" ")[1:]])

                frec_ids = self.vocab_frecs[words_ids]
                ordered_ids = np.argsort(frec_ids)[::-1]

                frec_ids = frec_ids[ordered_ids]
                words_ids = words_ids[ordered_ids]
                frec_ids = frec_ids/np.sum(frec_ids)
                
                with open(self.outputfile, 'a') as outfile:
                    outfile.write(str(len(words_ids)) + ' ')
                    outfile.write(' '.join([str(x[0]) + ':' + str(x[1]) for x in \
                                                    zip(words_ids, frec_ids)]))
                    outfile.write('\n')

