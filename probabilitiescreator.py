"""
Implements different methods to create probabilities distributions
of words over topics.
"""

import numpy as np

class Method1:
    def __init__(self, topicsfile, vocab_frecs, outputfile = 'method1.probs'):
        self.topicsfile = topicsfile
        self.vocab_frecs = vocab_frecs
        self.outputfile = outputfile

    def run(self):
        with open(self.outputfile, 'w') as f:
            pass # para borrar el archivo en caso de que exista

        with open(self.topicsfile, 'r') as f:
            for topic in f: # every line is a topic
                words_ids = np.array([int(x.split(":")[0]) for x in topic.split(" ")[1:]])
                frec_ids = self.vocab_frecs[words_ids]
                ordered_ids = np.argsort(frec_ids)[::-1]

                frec_ids = frec_ids[ordered_ids]
                words_ids = words_ids[ordered_ids]
                frec_ids = frec_ids/np.sum(frec_ids)
                
                with open(self.outputfile, 'a') as outfile:
                    outfile.write(str(len(words_ids)) + ' ')
                    outfile.write(' '.join([str(x[0]) + ':' + str(x[1]) for x in zip(words_ids, frec_ids)]))
                    outfile.write('\n')

