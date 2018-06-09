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
from collections import defaultdict

class Method1:
    """
    Assigns probabilities by assuming that all the occurrences of a word in the
    whole corpus belong to the topic; even if the word appears in different
    topics. And prints a file with the calculated probabilities.

    Thus, the probability that word 'w' appears given topic 't' is:
    p(w|t) = 
        (# of ocurrences of word 'w' in the corpus) /
        (sum of all occurrences of every word in topic 't' in the whole corpus)

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
                    outfile.write(
                        ' '.join(
                            [str(x[0]) + ':' + str(x[1]) for x in \
                                zip(words_ids, frec_ids)]))
                    outfile.write('\n')

class Method2:
    """
    A set of documents related to the topic should be first provided. This set
    is hereby regarded as the "topic's documents". It should be a subset of the
    corpus, and it's obtained by using the other tools in this repository. A
    document might be related to 0 or more topics.

    After being provided with the topic's documents, this method assigns
    probabilities by assuming that all the occurrences of a word
    in the topic's documents belong to the topic; even if the word and the
    document appears in different topics.

    Thus, the probability that word 'w' appears given topic 't' is:
    p(w|t) = 
        (# of ocurrences of word 'w' in the topic's documents) /
        (sum of all occurrences of every word in topic 't' in the topic's documents)

    """
    def __init__(self, topicsfile, tdfile, invcorpusfile):
        """
        Construct a new Method2 object
        
        :param topicsfile: a string with the path of the file where every line
        'n' is the set of the ids of the words that belong to topic 'n'

        :param tdfile: a string with the path of the file where every line 'n'
        is the set of the ids of the documents related to topic 'n'

        :param invcorpusfile: a string with the path of the file where the i-th
        line contains a list of the documents where the i-th word appears.

        :return: returns nothing
        """
        self.topicsfile = topicsfile
        self.tdfile = tdfile
        self.invcorpusfile = invcorpusfile

    def print_occurrences(self, outputfile):
        """
        Runs the method2 to create the file containing the occurences
        for each word in each topic, taking into account only the
        documents related to the topic (according to tdfile)

        :param outputfile: string with the path of the file where to print
        the occurrences per word per topic

        :return: returns nothing
        """


        with open(outputfile, "w") as opf:
            pass # TODO: Ver otra manera de borrar archivo si existe

        with open(self.topicsfile, "r") as tpf:
            with open(self.tdfile, "r") as tdf:
                for ii, line in enumerate(tdf): # each line is a topic
                    print(ii) #TODO: Turn this into a progress bar
                    line = line.split(" ")
                    if int(line[0]) == 0:
                        #if there are no documents related to the topic
                        # then no word is related to the topic...

                        words = [int(x.split(":")[0]) for x in \
                                tpf.readline().split(" ")[1:]]
                        counter = defaultdict(int)
                        for word in words:    
                            counter[word] = 0

                    else:
                        # if there are documents related to the topics, then...
                        counter = defaultdict(int)

                        docs = [int(x.split(":")[0]) for x in line[1:]]
                        #print(docs[0:min(10,len(docs))])
                        words = [int(x.split(":")[0]) for x in \
                                    tpf.readline().split(" ")[1:]]
                        #print(words[0:min(10,len(words))])

                        for word in words:
                            counter[word] = 0

                        with open(self.invcorpusfile, "r") as icf:                    
                            for w, wdocs in enumerate(icf):
                                if w in words:
                                    wdocs = [
                                             (
                                                int(x.split(":")[0]),
                                                int(x.split(":")[1]),
                                             ) for x in \
                                             wdocs.split(" ")[1:]
                                            ]
                                    #print(wdocs[0:min(10,len(wdocs))])
                                    # input()                            
                                    for doc, count in wdocs:
                                        if doc in docs:
                                            counter[w] += count

                    sorted_counter = sorted(counter.items(),
                        key = lambda x:(-x[1],x[0]))
                        # the dictionary is sorted in descending order by
                        # the word counter and ascending order by the index
                        # of the word in the case of counter ties


                    printstr = str(len(sorted_counter)) + " "
                    for i, x in enumerate(sorted_counter):
                        printstr += str(x[0])+":"+str(x[1])
                        if i != len(sorted_counter) - 1:
                            printstr += " "
                    printstr += "\n"

                    with open(outputfile, "a") as opf:
                        opf.write(printstr)                

    def occurences2probabilities(self, occurrencesfile, topicdistribfile):
        """
        Transform a occurences text file into a topic distribution text file.
        The input should be a text file where every line is a topic, with
        the words of that topic with their occurrences in the topic's documents.

        The output is a textfile where every line is a topic, with the words of
        that topic with the probabilities of the words.
        """
        with open(topicdistribfile, "w") as tdf:
            pass # TODO: Ver una mejor manera de borrar un archivo si existe

        with open(occurrencesfile, "r") as of:
            for line in of: #everyline is a topic
                counter = 0
                topic = []
                for wc in line.split(" ")[1:]:
                    word = int(wc.split(":")[0])
                    count = int(wc.split(":")[1])
                    counter += count
                    topic.append((word,count))

                printstr = str(len(topic)) + " "
                
                for i, wc in enumerate(topic):
                    if counter != 0:
                        proba = wc[1]/counter
                    else:
                        proba = 0 # because if counter == 0, then every word should
                                  # have probability = 0

                    printstr += str(wc[0]) + ":" + str(proba)
                    if i != len(topic) - 1:
                        printstr += " "
                    
                printstr += "\n"
                    
                with open(topicdistribfile, "a") as tdf:
                    tdf.write(printstr)
