# Antonio Velazquez
# 2018
# Written in Python 3.+

"""
Defines multiple ways to print easy-to-read files
for the topics and their assigned probability distributions
created by the probabilitiescreator module
"""

class MultipleFilesPrinter:
    """
    Prints one file per topic in the indicated path. Each file includes
    the words of the topic sorted by probability, their probability and other
    statistics.
    """
    def __init__(self, topicprobsfile, vocab_words, outputpath):
        """
        Construct a new MultipleFilesPrinter object
        :param topicprobsfile: file containing the probabilities, it is the
        output of the probabilitiescreator module

        :param vocab_words: list of words where the 'i'-th element is the word
        with id #i

        :param outputpath: string path where the topics files should be written

        :return: returns nothing
        """
        self.topicprobsfile = topicprobsfile        
        self.outputpath = outputpath
        self.vocab_words = vocab_words

    def print_topics(self, maxtopics = None):
        """
        Print the topics, one per file
        :param maxtopics: number of topics that should be printed, if empty,
        this method will print all topics

        :return: returns nothing
        """
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
                outfile.write(str(self.vocab_words[int(word_id)]) + " - " + \
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

