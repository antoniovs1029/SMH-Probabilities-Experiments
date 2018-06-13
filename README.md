I developed this code as part of my intership at the Institute of Research in Applied Mathematics and Systems (IIMAS)  at UNAM (México). It is supposed to work over the output gotten from the [Sampled-MinHashing](https://github.com/gibranfp/Sampled-MinHashing) tool created previously at the institute. The mentioned tool mines a given corpus and find several topics, where each topic is a set of words. The purpose of this repository is to experiment different ideas to assign probabilities to these words, so as to have a way to order them; for example, to know which words are more relevant, and the like.

Currently, this repository has only been tested in the **NIPS corpus** downloaded from knowceans, as done in the Sampled-Min-Hashing repository. The mentioned download includes files such as *nips.vocab* (the vocabulary of the corpus) and *nips.corpus* (which includes a bag of words representation of the documents). After running SMH over those files, other files are created such as *nips.models* (which includes the mined topics) and *nips.ifs* (the inverted index of *nips.corpus*). With all these files, and the code in this repository, other files are created representing the probability distributions of the topics.

To see an example, simply run the *demo1.py* file, by indicating an inputpath where the nips.vocab and nips.models shall be located. Or check the *probabilitiescreator.py* to have a look to the methods used to assign probabilities. Currently, the output looks like this:

![Results](imgs/cap0.png?raw=true "Results")
![Results](imgs/cap1.png?raw=true "Results")

# Installation and usage
No installation is needed, and no command line interface is provided. The code should be downloaded, and then the demos can be runned, provided the adequate inputs. Note that the code is written in Python 3.5+, and the required dependicies are listed in *requirements.txt*. 

In general, these are the steps to follow:
1. Provide the adequate input
2. Use a class from *probabilitiescreator.py* to generate a *topics distribution file* according to a desired method
3. Use a class from *printers.py* to print readable files based on the *topics distribution file* created in the previous step, as well as the documents related to each topic.

# Input and Output format and data
Following the scheme used in the [Sampled-MinHashing](https://github.com/gibranfp/Sampled-MinHashing) repository, the following format is used for most input and output files in this repository. Files contain lists of elements, one list in each row. The first number in the row is the number of elements in that list, then it's followed by the elements, where the first number is an id and the second element is giving some information of the id (for example, frecuencies, weights or other info.):
~~~~
6 3:9 4:8 7:5 12:1 16:5 18:5 
3 2:7 3:4 8:5
4 1:9 2:10 16:8 17:10
4 10:10 11:4 15:8 16:3
3 0:1 14:9 15:10
~~~~

Each approach to assign probabilities might need different inputs, and might create different outputs, but in general these are the files involved in this repository:

## Inputs
### From the Original Corpus
+ **Vocabulary file** - a file containing the vocabulary of the corpus, including the ids, the words, and the frequencies of the words inside the corpus. In this repository it has the extension *.vocab*

+ **Documents file** - a file containing the names of the documents of the corpus, and their respective id's. In this repository it has the extension *.docs*


### After using the Sampled-MinHashing tool
After using the [Sampled-MinHashing](https://github.com/gibranfp/Sampled-MinHashing) tool over some corpus, some files are created. Among them, the following are useful for this repository.

+ **Topics file** - a file where the i-th line is list of words related to the i-th topic. In this repository it has the extension *.models*
+ **Inverted Corpus File** - a file where the i-th line is the list of documents where the i-th word appears. In this repository it has the extension *.ifs*
+ **Inverted Word-Topics file** - a file where the i-th line is the list of topics where the i-th word appears. This file can be created by running the "ifs" command in the Sampled-MinHashing tool over the *.models* file. In this repository this file has the extension *.inverted_models*

## Intermediate files
These files are created while using this repository in order to get the output.
+ **Topic-documents file** - a file where the i-th line is the list of documents related to the i-th topic. In this repository it is often regarded as "tdfile".
+ **Occurrences file** - a file where the i-th line is the list of words related to the i-th topic, and each word is accompained with the number of times it has occurred in the context of the topic. Words are sorted by the number of occurrences.

## Output and printers
+ **Topics distributions file** - a file using the mentioned format, where each line is a topic, and each element is a word in the topic, followed by their probability given the topic. The words are sorted by probability. In this repository, the extension of this file is *.probs.txt*

The module *printers.py* includes different classes for printing the topics distributions and the documents related to the topic in plain text files, to gain better insight of the topics:
+ **topics.summary.txt** is a file where all topics are listed along with their most probable words. 
+ **documents.summary.txt** is a file where all topics are listed along with the documents that contain most of the words of the topic.
+ **/topics/** is a directory where several files are created, one per topic, listing all the words and their probabilities, as well as documents related to each topic.

# Implemented Methods
The idea of the repository is to explore different methods of assigning probabilities to the words given the topic. Currently there is only one implemented method.
+ **Method 1** - Assigns probabilities by assuming that all occurrences of the word in the corpus are produced by a given topic. This is somewhat a loose assumption, as it implies that every document where a given word appears is associated with every topic that contains such word. Future methods shall take into account that not every document is related to the topic.
+ **Method 2** - First select a subset of the corpus as the "documents related to a topic". Then calculate the frequencies of the words in a topic, but only on the corresponding documents. To select the subset of documents two approaches are provided: **Approach 2a** let the user set a percentage p%, if a document has equal or more than *p*% words of the topic, then the document is considered as related to the topic. **Approach 2b** let the user set a minimum of words *mw*, if a document has equal or more than *mw* words of the topic, then the document is considered as related to the topic. After using one of those approaches with high *p* or *mw*, then it might happen that no document is related to a topic, in such a case, then no word is related to the topic either.

# Compare
The *compare.py* script compares two probability distributions given to the same set of topics.

# Future Work
## Methods Ideas
+ To make duples pairing the words that belong to a topic, and finding the intersection of the sets of documents in which they appear. This should be repeated for every posible pairing of words. Then a parameter 'p' should be selected by the user, to select the documents that appear in p% of the pairs. This might be computationally heavy, depending on the topics sizes.
+ Another idea is to somehow include weights such as the tf-idf or the number of collisions that occured during the SMH with each word of a topic, in order to get the probabilities.
+ Also, inspired in the Gibbs Sampler used in LDA, one could make a sampler which assign to words one of the topics in which they appear, based in a formula which takes into account that words of the same topic might appear in the same document. 

## Others
+ Improve Exception Handling
+ Improve files and directories handling
+ Add output to binary files using Pickle, to save the probabilities distributions
+ Add more automatic statistics generators, such as: number of topics where a given word appears, number of words from the original vocabulary that doesn't appear in any topic, number of documents associated with a given topic, number of documents in which a word appears, largest topic, etc ...
+ Find a way to select which documents are associated with a topic. Probably using a metric to find the distance between a document and a topic (thinking both as tuple of words); and then using this metric to find a vectorial representation of the document based on its distances to the topics.
+ Create more interactive visualizations to work with the mined topics, and to compare them.
