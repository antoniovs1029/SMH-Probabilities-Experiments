"""
In this demo I show the usage of method 2
"""

from modulos.othertools import create_topics_documents, cut_topics_documents
from modulos.probabilitiescreator import Method2
from modulos.othertools import nips_get_vocab_words
from modulos.printers import DocumentsPrinter, TopicsDistributionPrinter

# Step -1: set paths to files

# inputs:
vocabfile = "./input/nips/nips.vocab"
docnamesfile = "./input/nips/nips.docs2" # tuve que crear el .docs2 porque el original estaba corrompido y no era utf8

topicsfile = "./input/v1/nips.models"
invcorpusfile = "./input/v1/nips.ifs" # documents related to each word
invwordtopics = "./input/v1/mios/nips.inverted_models"

# outputs:
out_dir = "./out/v1/method2b/"
tdfile = out_dir + "tdfile1.txt" # documents related to each topic
new_tdfile = out_dir + "tdfile2.txt"
occurrencesfile = out_dir + "topics.occurrences.txt"
topicdistribfile = out_dir + 'topics.probs.txt'
topicprobsummary = out_dir + "topics.summary.txt"
topicprobpath = out_dir + "topics/"
docsummary = out_dir + "documents.summary.txt"
docspath = out_dir + "topics/"


# Step 0: Set the documents related to each topic

# Step 0.1 Get all the documents where the words of each topic appear, print it
# in tdfile:
i = 0
print("Step", i)
create_topics_documents(topicsfile, invcorpusfile, tdfile) 

# Step 0.2 Cut the documents that don't meet the requirement of percentage or
# of minwords of the topic present in the document.
minwords = 2
cut_topics_documents(tdfile, new_tdfile, topicsfile, minwords = minwords)

# Step 1: Get the occurences and probabilities
i+=1
print("Step", i)
m2 = Method2(topicsfile, new_tdfile, invcorpusfile)
m2.print_occurrences(occurrencesfile)
m2.occurences2probabilities(occurrencesfile, topicdistribfile)

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
docprinter = DocumentsPrinter(new_tdfile, topicsfile, docnamesfile)
docprinter.print_summary_file(docsummary, n = 10)
docprinter.print_multiple_files(docspath)

print("END")
