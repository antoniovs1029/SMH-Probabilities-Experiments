"""
In this demo I show the usage of method 2
"""

from modulos.othertools import create_topics_documents, cut_topics_documents

# Step 0: Set the documents related to each topic

# Step 0.1 Get all the documents where the words of each topic appear, print it
# in tdfile:
topicsfile = "./input/v1/nips.models"
invcorpusfile = "./input/v1/nips.ifs" # documents related to each word
tdfile = "./input/v1/mios/nips.models_documents" # documents related to each topic
create_topics_documents(topicsfile, invcorpusfile, tdfile) 

# Step 0.2 Cut the documents that don't meet the requirement of percentage or
# of minwords of the topic present in the document.
new_tdfile = "./out/method2/method2.tdfile2.txt"

percent = .5
minwords = None
cut_topics_documents(tdfile, new_tdfile, topicsfile,
                    percent = percent, minwords = minwords)
