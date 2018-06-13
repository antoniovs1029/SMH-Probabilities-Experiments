"""
In this demo I show the usage of method 3
"""

from modulos.probabilitiescreator import Method3
from modulos.othertools import nips_get_vocab_words
from modulos.printers import DocumentsPrinter, TopicsDistributionPrinter
from modulos.othertools import create_topics_documents

vocabfile = "./input/nips/nips.vocab"
docnamesfile = "./input/nips/nips.docs2" # tuve que crear el .docs2 porque el original estaba corrompido y no era utf8
topicsfile = "./input/v1/nips.models"

invcorpusfile = "./input/v1/nips.ifs" # documents related to each word
invwordtopics = "./input/v1/mios/nips.inverted_models"

# outputs:
out_dir = "./out/v1/method3/"
tdfile = out_dir + "tdfile1.txt" # documents related to each topic
occurrencesfile = out_dir + "topics.occurrences.txt"
topicdistribfile = out_dir + 'topics.probs.txt'
topicprobsummary = out_dir + "topics.summary.txt"
topicprobpath = out_dir + "topics/"
docsummary = out_dir + "documents.summary.txt"
docspath = out_dir + "topics/"

# Step 1: Get the occurences and probabilities
i = 1
print("Step", i)
m3 = Method3(topicsfile, "./out/v1/method3/")
m3.run()

# Step 2: Print the probabilities
i+=1
print("Step",i)
vocab_words = nips_get_vocab_words(vocabfile)
tdp = TopicsDistributionPrinter(topicdistribfile,
                                vocab_words,
                                invwordtopics = invwordtopics)

tdp.print_topics_summary(topicprobsummary, maxwords = 10)
tdp.print_multiple_files(topicprobpath)


# Step 3: To gain more insight, get the documents related to each topic,
# according to method1 assumptions, and print them

i += 1
print("STEP ", i)
create_topics_documents(topicsfile, invcorpusfile, tdfile) 
docprinter = DocumentsPrinter(tdfile, topicsfile, docnamesfile)
docprinter.print_summary_file(docsummary, n = 10)
docprinter.print_multiple_files(docspath)

print("END")
