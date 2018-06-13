from modulos.probabilitiescomparer import compare_topics
from modulos.othertools import  nips_get_vocab_words

vocabfile = "./input/nips/nips.vocab"
topicfile1 = "./out/v1/method1/method1.probs.txt"
topicfile2 = "./out/v1/method2a/topics.probs.txt"
outpath = "./out/comparison/1/"

vocabulary = nips_get_vocab_words(vocabfile)

compare_topics(outpath, topicfile1, topicfile2, vocabulary)
