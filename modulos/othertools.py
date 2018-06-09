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

def create_topics_documents(topicsfile, invcorpusfile, tdfile):
    """
    Prints a file with the list of documents related to each topic.
    To do that, for every word of the topic, add any document where
    that word appears. Even more, put the number of distinct words
    that appear in the document, and that are part of each topic.

    :param topicsfile: string of the path where the file containing the topics
    is located
    :para invcorpusfile: string of the path  where the file containing the
    inverted corpus is located. That is, the file where each line is a word
    followed by the list of documents where it appears.
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

def cut_topics_documents(tdfile, new_tdfile, topicsfile,
                        percent = None, minwords = None):
    """
    It takes a text file (tdfile) where the i-th line contains a list of the
    id's of the documents related to topic i. Each document is accompained by
    the number of distinct topic words that appear in the document. This
    document is actually the output of the create_topics_documents in
    this module.

    For every topic, this function cuts-off the documents that don't meet the
    requirement set by the parameter percent or the parameter minwords.

    That is, if percent = 50, then any document that doesn't have 50% of the
    words of the topic will be cut out from the list.

    If minwords = 5, then any document that doesn't have 5 words from the topic
    will be eliminated from the list.

    The remaning lists are printed into a new file (new_tdfile)

    For consistency, only percent or minwords shall have a value (None is default
    for both) if both have a value, or neither have a value, then an error is
    raised.

    Evenmore, If percent = 0 or minwords = 0, by definition, the original tdfile
    is going to be copied integrally.

    If minwords is lower than the number of words in a topic, then the minword
    cutoff for the topic will be the number of words in the topic.

    :param tdfile: string with the path to the input file as described bove

    :param new_tdfile: string with the path to the output file as described above

    :param topicsfile: string to the file where each line is a topic, and the
    first number in the line is the number of words in the topic

    :param percent: percentage for cutoff as described above. Any number between
    0 and 1 will do.

    :param minwords: non-negative integer for cutoff as described above

    :return Returns nothing  
    """

    #TODO: Mejorar mi manejo de errores/excepciones aquí...
    if percent is None and minwords is None:
        print("ERROR: There must be a value for the parameter percent OR" + \
              " for the parameter minwords. No value was given for neither"+\
              " of them.")
        exit()

    if percent is not None and minwords is not None:
        print("ERROR: There must be a value for the parameter percent OR"+ \
              " for the parameter minwords. NOT for both.")
        exit()

    if percent is not None:
        if percent < 0 or percent > 1:
            print("ERROR: Percent should be a number between 0 and 1")
            exit()
    else:
        if minwords < 0 or type(minwords) != type(5):
            print("ERROR: Minwords should be a non negative integer")
            exit()

    with open(new_tdfile, "w") as ntdf:
        pass #TODO: encontrar otra manera de borrar el archivo si existe

    with open(tdfile, "r") as tdf:
        with open(topicsfile, "r") as tpf:
            for line in tdf: # each line is a topic
                nwords = int(tpf.readline().split(" ")[0]) # number of words in topic

                # Choose the min words for the topic:                
                if percent is not None:
                    minwordstopic = int(percent*nwords)
                else:
                    minwordstopic = min(nwords, minwords) # if minwords < nwords

                line = line.strip("\n") # quitar el salto al final de la linea
                docs = line.split(" ")[1:]
                new_docs = []
                for doc in docs:
                    doc_count = int(doc.split(":")[1])
                    if doc_count >= minwordstopic:
                        new_docs.append(doc)
                    else:
                        break # since the documents are ordered by the number of
                              # words, the for loop can break as soon as a doc
                              # doesn't meet the requirement

                with open(new_tdfile, "a") as ntdf:
                    ntdf.write(
                        str(len(new_docs)) +
                        " " +
                        " ".join(new_docs) +
                        "\n"
                    )
