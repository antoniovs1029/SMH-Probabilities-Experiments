I developed this code as part of my intership at the Institute of Research in Applied Mathematics and Systems (IIMAS)  at UNAM (México). It is supposed to work over the output gotten from the [Sampled-Min-Hashing](https://github.com/gibranfp/Sampled-MinHashing) tool created previously at the institute. The mentioned tool mines a given corpus and find several topics, where each topic is a set of words. The purpose of this repository is to experiment different ideas to assign probabilities to these words, so as to have a way to order them; for example, to know which words are more relevant, and the like.

Currently, this repository has only been tested in the **NIPS corpus** downloaded from knowceans, as done in the Sampled-Min-Hashing repository. The mentioned download includes files such as *nips.vocab* (the vocabulary of the corpus) and *nips.corpus* (which includes a bag of words representation of the documents). After running SMH over those files, other files are created such as *nips.models* (which includes the mined topics) and *nips.ifs* (the inverted index of *nips.corpus*). With all these files, and the code in this repository, other files are created representing the probability distributions of the topics.

To see an example, simply run the *demo.py* file, by indicating an inputpath where the nips.vocab and nips.models shall be located. Or check the *probabilitiescreator.py* to have a look to the methods used to assign probabilities.

# Installation and usage
No installation is needed, and no command line interface is provided. The code should be downloaded, and then the tools can be used by following the example of *demo.py*, and providing the adequate inputs (read below).

# Input and Output format and data
Following the Sampled-Min-Hashing scheme, the following format is used for most input and output files in this repository. Files contain lists of elements, one list in each row. The first number in the row is the number of elements in that list, then it's followed by the elements, where the first number is an id and the second element is giving some information of the id (for example, frecuencies, weights or other info.):
~~~~
6 3:9 4:8 7:5 12:1 16:5 18:5 
3 2:7 3:4 8:5
4 1:9 2:10 16:8 17:10
4 10:10 11:4 15:8 16:3
3 0:1 14:9 15:10
~~~~

## Inputs
+ **Vocabulary Frecuencies Numpy Array** - a numpy array where the i-th element has the frecuency of the word with id #i. For *demo.py*, this array is created from the previously downloaded *nips.vocab* file.
+ **Vocabulary Words List** - a python list where the i-th element has the string of the word with id #i. For the *demo.py* this list is created from the *nips.vocab* file.
+ **Topics file** - a file using the mentioned format, where each line is a topic, and each element is a word in the topic. After using the  Sampled-Min-Hashing tool, this is the *nips.models* file.

## Output and printers
+ **Topics distributions file** - a file using the mentioned format, where each line is a topic, and each element is a word in the topic, followed by their probability given the topic. The words are sorted by probability. By default, the extension of this file is *.probs*

The module *topicsprinter.py* includes different classes for printing the topics distributions file:
+ **Multiple Files Printer** - Prints a file for each topic, listing the words of the topic sorted by their probabilities, and adding some other statistics.
+ **Single File Summary Printer** - Prints a file with a summary of all topics; that is, a list of the top words of each topic and some statistics.

# Implemented Methods
The idea of the repository is to explore different methods of assigning probabilities to the words given the topic. Currently there is only one implemented method.
+ **Method 1** - Assigns probabilities by assuming that all occurrences of the word in the corpus are produced by a given topic. This is somewhat a loose assumption, as it implies that every document where a word appears is associated with every topic that contains the word. Future methods shall take into account that not every document is related to the topic.

# Future Work
## Methods Ideas
+ One approach is to think that only documents that contain 'm' words of a given topic are related to this topic. The user shall indicate the 'm' parameter, and then all the documents associated with a topic should be found. Later, probabilities could be calculated, by only looking at the subset of the corpus formed by the documents associated with a topic.
+ Similar to the approach of the previous point, is to make duples pairing the words that belong to a topic, and finding the intersection of the sets of documents in which they appear. This should be repeated for every posible pairing of words. Then a parameter 'p' should be selected by the user, to select the documents that appear in p% of the pairs. This might be computationally heavy, depending on the topics sizes.
+ Another idea is to somehow include weights such as the tf-idf or the number of collisions that occured during the SMH with each word of a topic, in order to get the probabilities.

## Others
+ Add output to binary files using Pickle, to save the probabilities distributions
+ Add more automatic statistics generators, such as: number of topics where a given word appears, number of words from the original vocabulary that doesn't appear in any topic, number of documents associated with a given topic, number of documents in which a word appears, largest topic, etc ...
+ Find a way to select which documents are associated with a topic
+ Create more interactive visualizations to work with the mined topics, and to compare them.