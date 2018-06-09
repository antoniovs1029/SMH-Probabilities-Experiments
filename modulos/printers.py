# Antonio Velazquez
# 2018
# Written in Python 3.+

"""
Defines multiple ways to print easy-to-read files.
For the topics and their assigned probability distributions
created by the probabilitiescreator module, as well as
other kind of lists, such as the list of documents related to
a topic.
"""

class DocumentsPrinter:
    """
    A class to print information of documents related to topics
    in files.
    """

    def __init__(self, tdfile, topicsfile, docnamesfile):
        """
        Construct a new DocumentsPrinter object

        :param tdfile: a string with the path of the
        text file containing the list of documents' ids related
        to a topic. Each line is a topic, and each element
        in the list is the id of a document, together with
        the number of times that distinct words of the topic
        appear in the document. The documents should be listed
        in descending order, according to their respective
        counters.

        :param topicsfile: a string with the path of the text
        file containing the topics. Each line is a topic,
        followed by the list of the words that belong to the
        topic.

        :param docnamesfile: a string with the path of the
        text file that contains the titles of the documents.
        The i-th line has the title of the i-th document.
        """
        self._tdfile = tdfile
        self._topicsfile = topicsfile
        self._docnamesfile = docnamesfile


    def print_summary_file(self, outputfile, n = 5):
        """
        Prints the titles of the documents to the outputfile
        :param outputfile: string to the path of the file where to print the
        titles
        :param n: Optional. Number of titles to print for each document.
        Only the top n titles will be printed. Default is n
        """
        
        # For faster retrieval, the names of the docs are loaded into memory first
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
                    docs_number = int(line[0])
                    docs = line[1:min(len(line),n)] # in case n is bigger 
                                # than the number of
                                # documents

                    # Warning: if docs_number == 0, then docs = ['\n'] ; remember this in
                    # case of errors

                    with open(outputfile, "a") as out:
                        out.write("Topic #" + str(i) +": - with " + \
                                    str(docs_number) + " related documents and " +\
                                    str(words_in_topic) + " words\n")
                        
                        if docs_number == 0:
                            out.write("No documents related to the topic!")
                        else:
                            for doc in docs:
                                doc, count = doc.split(":")
                                doc = int(doc)
                                count = int(count)

                                percent = (count / words_in_topic)*100
                                out.write(docnames[doc] + ' %.2f'%percent + "%\n")

                        out.write("\n")

    def print_multiple_files(self, outputdir, maxtopics = None):
        """
        Print the title of the documents related to each topics, one topic per file

        :param outputdir: string to the directory where to put the files.

        :param maxtopics: number of topics that should be considered, if empty,
        this method will print the documents of all topics

        :return: returns nothing
        """
        # For faster retrieval, the names of the docs are load into memory first
        docnames = []
        with open(self._docnamesfile, "r") as dnf:
            for line in dnf:
                docnames.append(line[:-1]) #take out the last character ("\n")

        with open(self._topicsfile, "r") as tpf:
            with open(self._tdfile, "r") as tdf:
                for i, line in enumerate(tdf):
                    if maxtopics is not None and i > maxtopics:
                        break;

                    words_in_topic = int(tpf.readline().split(" ")[0])
                    line = line.split(" ")
                    docs_number = int(line[0])
                    docs = line[1:]

                    outputfile = outputdir + "topic" + str(i) + "_documents.txt"

                    with open(outputfile, "w") as out:
                        out.write("Topic #" + str(i) +": - with " + \
                                    str(docs_number) + " related documents and " +\
                                    str(words_in_topic) + " words\n")
                        
                        if docs_number == 0:
                            out.write("No documents related to the topic!")
                        else:
                            for doc in docs:
                                doc, count = doc.split(":")
                                doc = int(doc)
                                count = int(count)

                                percent = (count / words_in_topic)*100
                                out.write(docnames[doc] + ' %.2f'%percent + "%\n")

                        out.write("\n")

class TopicsDistributionPrinter:
    """
    Prints files related to the to topics distributions generated by the
    probabilitiescreator module.
    """

    def __init__(self, topicprobsfile, vocab_words, invwordtopics = None):
        """
        Construct a new TopicDistributionPrinter object
        :param topicprobsfile: file containing the probability distribution of the
        topics, it is the output of the probabilitiescreator module

        :param vocab_words: list of words where the 'i'-th element is the word
        with id #i

        :param invwordtopics: Optional. string with the path to the file where
        the i-th line has a list of the topics where the i-th word appears.

        :return: returns nothing
        """
        self.topicprobsfile = topicprobsfile        
        self.vocab_words = vocab_words
        self.invwordtopics = invwordtopics

    def print_multiple_files(self, outputdir, maxtopics = None):
        """
        Print the topics, one per file
        :param outputdir: string with the  path to the directory where the
        files are going to be printed

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
                    self.iwt.append(int(line.split(" ")[0]))
                    # the first element in the line is the number of elements in the line

        self._prepare_output_path()
        with open(self.topicprobsfile, 'r') as f:
            for i,topic in enumerate(f):
                if maxtopics and i == maxtopics-1:
                    break
                self._print_one_topic_file(outputdir, i,topic.split(" "))

    def _print_one_topic_file(self, outputdir, i, topic):
        with open(outputdir + "topic" + str(i) + ".txt", 'w') as outfile:
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

    def print_topics_summary(self, outputfile, maxwords = 10):
        """
        :param maxwords: integer, number of top words to output for every topic
        :return: returns nothing
        """
        with open(outputfile, 'w') as f:
            pass # se borra el archivo si existe

        # TODO: Ver otra manera de borrar el archivo si existe

        with open(self.topicprobsfile, 'r') as f:
            for i,topic in enumerate(f):
                self._print_one_topic_summary(outputfile, i, topic.split(" "), maxwords)

    def _print_one_topic_summary(self, outputfile, i, topic, maxwords):
        with open(outputfile, 'a') as outfile:
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
