# Antonio Velazquez
# 2018
# Written in Python 3.+

"""
Defines multiple ways to print easy-to-read files
for the topics and their assigned probability distributions
created by the probabilitiescreator module. As well as
other kind of lists, such as the list of documents related to
a topic.
"""

class SingleFileDocumentsPrinter:
    """
    Prints a file with the the top documents related with a printer.
    Along with the % of words of the topic that appear in the document.
    """
    def __init__(self, tdfile, topicsfile, docnamesfile):
        """
        Construct a new SingleFileDocumentsPrinter object

        :param tdile: list of documents related to a topic
        :param topicsfile: list of words related to a topic
        :param docnamesfile: names of the documents
        :param outputfile: path of the file where to print the documents titles  
        """
        self._tdfile = tdfile
        self._topicsfile = topicsfile
        self._docnamesfile = docnamesfile

    def print_file(self, outputfile, n = 5):
        """
        Prints the titles of the documents to the outputfile
        :param outputfile: string to the path of the file where to print the
        titles
        """
        
        # For faster retrieval, the names of the docs are load into memory first
        docnames = []
        with open(self._docnamesfile, "r") as dnf:
            for line in dnf:
                docnames.append(line[:-1]) #take out the last character ("\n")

        with open(outputfile, "w") as out:
            pass # TODO: Find a better way to erase a file if it exists

        with open(self._topicsfile, "r") as tpf:
            with open(self._tdfile, "r") as tdf:
                for i, line in enumerate(tdf):
                    words_in_topic = int(tpf.readline().split(" ")[0])
                    line = line.split(" ")
                    docs_number = line[0]
                    docs = line[1:min(len(line),n)] # in case n is bigger 
                                # than the number of
                                # documents

                    with open(outputfile, "a") as out:
                        out.write("Topic #" + str(i) +": - with " + \
                                    str(docs_number) + " related documents and " +\
                                    str(words_in_topic) + " words\n")
                        
                        for doc in docs:
                            doc, count = doc.split(":")
                            doc = int(doc)
                            count = int(count)

                            percent = (count / words_in_topic)*100
                            out.write(docnames[doc] + ' %.2f'%percent + "%\n")

                        out.write("\n")

class MultipleFilesPrinter:
    """
    Prints one file per topic in the indicated path. Each file includes
    the words of the topic sorted by probability, their probability and other
    statistics.
    """
    def __init__(self, topicprobsfile, vocab_words, outputpath, invwordtopics = None):
        """
        Construct a new MultipleFilesPrinter object
        :param topicprobsfile: file containing the probabilities, it is the
        output of the probabilitiescreator module

        :param vocab_words: list of words where the 'i'-th element is the word
        with id #i

        :param outputpath: string path where the topics files should be written

        :param invwordtopics: Optional. string path to the file where the i-th
        line has a list of the topics where the i-th word appears.

        :return: returns nothing
        """
        self.topicprobsfile = topicprobsfile        
        self.outputpath = outputpath
        self.vocab_words = vocab_words
        self.invwordtopics = invwordtopics

    def print_topics(self, maxtopics = None):
        """
        Print the topics, one per file
        :param maxtopics: number of topics that should be printed, if empty,
        this method will print all topics

        :return: returns nothing
        """

        # If there's a file where to find the list of topics related to a word:
        # Load it in memory:
        if self.invwordtopics is not None:
            self.iwt = [] # number of topics related to each word
            with open(self.invwordtopics, "r") as f:
                for line in f:
                    self.iwt.append(int(line.split(" ")[0])) # the first element
                                                             # in the line is the
                                                             # number of elements
                                                             # in the line

        self._prepare_output_path()
        with open(self.topicprobsfile, 'r') as f:
            for i,topic in enumerate(f):
                if maxtopics and i == maxtopics-1:
                    break
                self._print_one_topic(i,topic.split(" "))

    def _print_one_topic(self, i, topic):
        with open(self.outputpath + "topic" + str(i) + ".txt", 'w') as outfile:
            outfile.write(str(i) + ' - # Words: ' + str(topic[0]) + '\n')
            for x in topic[1:]:
                word_id, word_prob = x.split(":")
                ntopics = "?"
                if self.invwordtopics is not None:
                    ntopics = self.iwt[int(word_id)]
                    ntopics = str(ntopics)

                outfile.write(str(\
                    self.vocab_words[int(word_id)]) + \
                    " (id: " + word_id + "," +\
                    " # topics: " + ntopics + ")"\
                    " - Prob: " + \
                    str(word_prob))
                outfile.write('\n')
            outfile.write("\n")

    def _prepare_output_path(self):
        # TODO: Create this method to erase the contents of the path,
        # if they exist already, and to create the directory if it doesn't exist
        pass        

class SingleFileSummaryPrinter:
    """
    Prints one file that summarizes all the topics by outputing the top words
    of the topic one word per line, along with some statistics.
    """
    def __init__(self, topicprobsfile, vocab_words, outputfile):
        """
        Construct a new SingleFileSummaryPrinter object

        :param topicprobsfile: file containing the probabilities, it is the
        output of the probabilitiescreator module

        :param vocab_words: list of words where the 'i'-th element is the word
        with id #i

        :param outputfile: string path where the topics summary should be written

        :return: returns nothing
        """
        self.topicprobsfile = topicprobsfile        
        self.outputfile = outputfile
        self.vocab_words = vocab_words

    def print_topics(self, maxwords = 10):
        """
        :param maxwords: integer, number of top words to output for every topic
        :return: returns nothing
        """
        with open(self.outputfile, 'w') as f:
            pass # se borra el archivo si existe

        # TODO: Ver otra manera de borrar el archivo si existe

        with open(self.topicprobsfile, 'r') as f:
            for i,topic in enumerate(f):
                self._print_one_topic(i, topic.split(" "), maxwords)

    def _print_one_topic(self, i, topic, maxwords):
        with open(self.outputfile, 'a') as outfile:
            outfile.write('Topic #' + str(i) + ' - # Words: ' + \
                                                str(topic[0]) + '\n')
            if maxwords > len(topic) - 1:
                maxwords = len(topic) - 1

            for x in topic[1:maxwords + 1]:
                word_id, word_prob = x.split(":")
                outfile.write(str(self.vocab_words[int(word_id)]) + " - " + \
                                                                str(word_prob))
                outfile.write('\n')
            outfile.write("\n")

