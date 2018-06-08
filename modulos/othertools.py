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

def create_topics_documents1(topicsfile, invcorpusfile, tdfile):
    """
    Prints a file with the list of documents related to each topic.
    To do that, for every word of the topic, add any document where
    that word appears. Even more, put the number of distinct words
    that appear in the document, and that are part of each topic.

    :param topicsfile: string of the path where the file containing the topics
    is located
    :para invcorpusfile: string of the path  where the file containing the
    inverted corpus is located (that is, the lists of documents where the words
    appear)
    :param tdfile: string of the path where the files is going to be written
    :return Returns nothing
    """

    from collections import defaultdict

    # load the invcorpusfile into memory, for faster retrieval
    # if the corpus is too big, this might break...
    words_docs = [] # it's a list of lists; where the i-th element contains the
                    # list of documents where the i-th word appeared

    with open(invcorpusfile, "r") as icf:
        for i, line in enumerate(icf):
            word_docs = []
            for doc in line.split(" ")[1:]:
                word_docs.append(int(doc.split(":")[0])) # adds only the document, 
                # without the frequency; the id of the document is added as an int
            words_docs.append(word_docs)

    
    topics = []

    with open(tdfile, "w") as tdf:
        with open(topicsfile, "r") as tpf:
            for line in tpf:
                topic_doc_counter = defaultdict(int)
                for word in line.split(" ")[1:]:
                    word = word.split(":")[0] # here the weight doesn't matter
                    for doc in words_docs[int(word)]:
                        topic_doc_counter[doc] += 1
                
                sorted_d = sorted(topic_doc_counter.items(),
                    key = lambda x: (-x[1],x[0]))
                    # the dictionary is ordered in descending order by the
                    #counter and ascending by the index of the document
                    # in the case of counter ties.

                tdf.write(str(len(sorted_d)) + " ")                

                for i, x in enumerate(sorted_d):
                    tdf.write(str(x[0])+":"+str(x[1]))
                    if i != len(sorted_d) - 1:
                        tdf.write(" ")
                tdf.write("\n")


