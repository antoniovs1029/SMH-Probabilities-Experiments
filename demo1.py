"""
In this demo I show the general usage of the tools in this repository, to get
the topics with probabilities distributions using method1.

Method1 consists in believing that every occurrence of a word in a copus,
is related to any topic where the word is a member.
"""

from modulos.othertools import nips_get_vocab_frecuencies, nips_get_vocab_words
from modulos.probabilitiescreator import Method1

from modulos.othertools import create_topics_documents
from modulos.printers import DocumentsPrinter, TopicsDistributionPrinter

vocabfile = "./input/nips/nips.vocab"
topicsfile = "./input/v1/nips.models"

# Step 1: Create frecuencies and words arrays
i = 1
print("STEP ", i)

vocab_frecs = nips_get_vocab_frecuencies(vocabfile)
vocab_words = nips_get_vocab_words(vocabfile)
print(vocab_frecs[0:10])
print(vocab_words[0:10])

# Step 2: Use method1 to assign probabilities, printing them in the
# method1.probs.txt file

i += 1
print("STEP ", i)

topicdistribfile = './out/method1/method1.probs.txt'
m1 = Method1(topicsfile, vocab_frecs, outputfile = topicdistribfile)
m1.run()

# Step 3: Print the topics
i += 1
print("STEP ", i)

tdp = TopicsDistributionPrinter(topicdistribfile,
                                vocab_words,
                                invwordtopics = "./input/v1/mios/nips.inverted_models")

tdp.print_topics_summary("./out/method1/method1.summary.txt", maxwords = 10)
tdp.print_multiple_files("./out/method1/method1distribs/")


# Step 4: To gain more insight, get the documents related to each topic,
# according to method1 assumptions, and print them

i += 1
print("STEP ", i)


# step 4.1 : create the tdfile:
invcorpusfile = "./input/v1/nips.ifs" # documents related to each word
tdfile = "./input/v1/mios/nips.models_documents" # documents related to each topic
create_topics_documents(topicsfile, invcorpusfile, tdfile) 

#step 4.2 : print the documents:
docnamesfile = "./input/nips/nips.docs2" # tuve que crear el .docs2 porque el original
                                        # estaba corrompido y no era utf8

docprinter = DocumentsPrinter(tdfile, topicsfile, docnamesfile)
docprinter.print_summary_file("./out/method1/documents_by_topic.txt" , n = 10)
docprinter.print_multiple_files("./out/method1/method1distribs/")

print("END")
