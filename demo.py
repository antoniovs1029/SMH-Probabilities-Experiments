from othertools import NipsVocabParser
from probabilitiescreator import Method1
from topicsprinters import MultipleFilesPrinter, SingleFileSummaryPrinter

inputdir = "/home/antonio/ServicioSocial/3_programas-originales/knowceans-ilda/nips/"
vocabfile = inputdir + "nips.vocab"
topicsfile = inputdir + "nips.models"

# Step 1: Create frecuencies and words arrays
getvocab = NipsVocabParser(vocabfile)
vocab_frecs = getvocab.get_vocab_frecuencies()
vocab_words = getvocab.get_vocab_words()
print(vocab_frecs[0:10])
print(vocab_words[0:10])

# Step 2: Try out a method to assign probabilities
m1 = Method1(topicsfile, vocab_frecs, outputfile = './out/method1/method1.probs')
m1.run()

# Step 3: Print the topics
# In different files:
outputpath = "./out/method1/method1distribs/"
mfp1 = MultipleFilesPrinter('./out/method1/method1.probs', vocab_words, outputpath)
mfp1.print_topics()

# In one summary file:
sfsp1 = SingleFileSummaryPrinter('./out/method1/method1.probs', vocab_words, './out/method1/method1.summary')
sfsp1.print_topics()
