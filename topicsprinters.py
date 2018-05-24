"""
Defines multiple ways to print easy-to-read files
for the topics and their assigned probability distributions
"""

class MultipleFilesPrinter:
    """
    Prints one file per topic in the indicated path.
    """
    def __init__(self, topicprobsfile, vocab_words, outputpath):
        self.topicprobsfile = topicprobsfile        
        self.outputpath = outputpath
        self.vocab_words = vocab_words

    def print_topics(self, maxtopics = None):
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
                outfile.write(str(self.vocab_words[int(word_id)]) + " - " + str(word_prob))
                outfile.write('\n')
            outfile.write("\n")

    def _prepare_output_path(self):
        pass        

class SingleFileSummaryPrinter:
    """
    Prints one file that summarizes all the topics by outputing the top words of the topic
    one word per line
    """
    def __init__(self, topicprobsfile, vocab_words, outputfile):
        self.topicprobsfile = topicprobsfile        
        self.outputfile = outputfile
        self.vocab_words = vocab_words

    def print_topics(self, maxwords = 10):
        with open(self.outputfile, 'w') as f:
            pass # se borra el archivo si existe

        with open(self.topicprobsfile, 'r') as f:
            for i,topic in enumerate(f):
                self._print_one_topic(i, topic.split(" "), maxwords)

    def _print_one_topic(self, i, topic, maxwords):
        with open(self.outputfile, 'a') as outfile:
            outfile.write('Topic #' + str(i) + ' - # Words: ' + str(topic[0]) + '\n')
            if maxwords > len(topic) - 1:
                maxwords = len(topic) - 1

            for x in topic[1:maxwords + 1]:
                word_id, word_prob = x.split(":")
                outfile.write(str(self.vocab_words[int(word_id)]) + " - " + str(word_prob))
                outfile.write('\n')
            outfile.write("\n")

