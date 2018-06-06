"""
In this demo I show the usage of method 2
"""

from modulos.othertools import nips_get_vocab_frecuencies, nips_get_vocab_words, create_topics_documents1
from modulos.probabilitiescreator import Method1
from modulos.topicsprinters import MultipleFilesPrinter, SingleFileSummaryPrinter

vocabfile = "./input/nips/nips.vocab"
topicsfile = "./input/v1/nips.models"
invcorpusfile = "./input/v1/nips.ifs"

# Step 0: Create a list of documents related to a topic
tdfile = "./input/v1/mios/nips.models_documents"
create_topics_documents1(topicsfile, invcorpusfile, tdfile)

"""
# Step 1: Create frecuencies and words arrays
vocab_frecs = nips_get_vocab_frecuencies(vocabfile)
vocab_words = nips_get_vocab_words(vocabfile)
print(vocab_frecs[0:10])
print(vocab_words[0:10])

# Step 2: Try out a method to assign probabilities
probs_path = './out/method1/method1.probs.pickle'
m1 = Method1(topicsfile, vocab_frecs, outputfile = probs_path)
m1.run()

# Step 3: Print the topics
# In different files:
mfp1 = MultipleFilesPrinter(probs_path, vocab_words, "./out/method1/method1distribs/")
mfp1.print_topics()

# In one summary file:
sfsp1 = SingleFileSummaryPrinter(probs_path, vocab_words, './out/method1/method1.summary.text')
sfsp1.print_topics()
"""
