"""
In this demo I show the general usage of the tools in this repository, to get
the topics with probabilities distributions using method1.

Method1 consists in believing that every occurrence of a word in a copus,
is related to any topic where the word is a member.
"""

from modulos.othertools import nips_get_vocab_frecuencies, nips_get_vocab_words
from modulos.probabilitiescreator import Method1
from modulos.topicsprinters import MultipleFilesPrinter, SingleFileSummaryPrinter

vocabfile = "./input/nips/nips.vocab"
topicsfile = "./input/v1/nips.models"

# Step 1: Create frecuencies and words arrays
vocab_frecs = nips_get_vocab_frecuencies(vocabfile)
vocab_words = nips_get_vocab_words(vocabfile)
print(vocab_frecs[0:10])
print(vocab_words[0:10])

# Step 2: Try out a method to assign probabilities
probs_path = './out/method1/method1.probs.txt'
m1 = Method1(topicsfile, vocab_frecs, outputfile = probs_path)
m1.run()

# Step 3: Print the topics
# In different files:
mfp1 = MultipleFilesPrinter(probs_path, vocab_words,
                            "./out/method1/method1distribs/",
                            invwordtopics = "./input/v1/mios/nips.inverted_models")
mfp1.print_topics()

# In one summary file:
sfsp1 = SingleFileSummaryPrinter(probs_path, vocab_words,
                                './out/method1/method1.summary.text')
sfsp1.print_topics()

# Step 4: To gain more insight, get the documents related to each topic,
# according to method1 assumptions

from modulos.othertools import create_topics_documents1
from modulos.topicsprinters import SingleFileDocumentsPrinter

# step 4.1 : create the tdfile:
invcorpusfile = "./input/v1/nips.ifs" # documents related to each word
tdfile = "./input/v1/mios/nips.models_documents" # documents related to each topic
create_topics_documents1(topicsfile, invcorpusfile, tdfile) 


#step 4.2 : print the documents_by_topic file:
docnamesfile = "./input/nips/nips.docs2" # tuve que crear el .docs2 porque el original
                                        # estaba corrompido y no era utf8
outputfile = "./out/method1/documents_by_topic.txt" # titles of documents related to each topic
sfdp = SingleFileDocumentsPrinter(tdfile, topicsfile, docnamesfile)
n = 10
sfdp.print_file(outputfile, n)

print("END")
