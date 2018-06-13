# Antonio Velazquez
# 2018
# Written in Python 3.+

"""
Module that defines tools to compare two probabilities distributions created
for the same topic.
"""

def line_to_dictdistrib(line):
    """
    :param line, a string list of elements representing a probability distribution
    :return a dictionary where the key is the id of the word, and the value is
    the probability of such a word
    """
    dictdistrib = dict()
    for elem in line.split(" ")[1:]:
        k, v = elem.split(":")
        dictdistrib[int(k)] = float(v)
    return dictdistrib

def compare_distribs(distrib1, distrib2):
    """
    :param distrib1, distrib2: dictionaries of probabilities distributions of the
    same topic. Where key's are word's id's and values are their probability.
    :return A tuple:
    The first element is the total difference in probabilities
    of all the elements of the topic (float).
    
    The second element is a list of tuples, where each tuple is a pair
    ('word id', 'probability difference'). The tuples are sorted by
    descending order of the probability difference.
    """
    if distrib1.keys() != distrib2.keys():
        print("Can not compare diferent topics")
        exit()

    difdict = dict()
    total_dif = 0
    for k in distrib1.keys():
        dif = abs(distrib1[k] - distrib2[k])
        difdict[k] = dif
        total_dif += dif

    sorted_difdict = sorted(difdict.items(), key = lambda x:(-x[1],x[0]))

    return total_dif, sorted_difdict

def print_comparison(outfile, difdict, vocabulary):
    """
    Prints a comparison between two probability distributions of the same topic

    :param outfile: string with the path of the file where to print the results

    :param difdict: a dictionary containing the differences of each word in
    the topic. The keys are the words' id's and the value is their respective
    difference in their probability distributions.

    :param vocabulary: a list of strings where the i-th element is the word
    with index #i.

    :return Returns Nothing
    """
    printstr = ""    
    for wid, dif in difdict:
        printstr += vocabulary[wid] + " Dif: " + str(dif) + '\n'

    with open(outfile, "w") as out:
        out.write(printstr)

def compare_topics(outpath, topicdistribfile1, topicdistribfile2, vocabulary):
    """
    Compares 2 probabilities distributions for each topic, and prints files
    for each topic, and a summary file in the outpath.

    :param outpath: a string with the path where the output is going to be
    created.

    :params topicdistribfile1 and topicdistribfile2: each file has a line for
    each topic, and in the line there's the probability distribution of that
    topic. Both files should refer to the same topics.

    :param vocabulary: a list of strings where i-th element is the word with
    if #i.

    :return Returns Nothing
    """
    topics_dif = []
    with open(topicdistribfile1, "r") as tp1:
        with open(topicdistribfile2, "r") as tp2:
            for i, line1 in enumerate(tp1):
                line2 = tp2.readline()
                dd1 = line_to_dictdistrib(line1)
                dd2 = line_to_dictdistrib(line2)
                
                total_dif, difdict = compare_distribs(dd1, dd2)
                print_comparison(outpath + "/topics/topic" + str(i) \
                    + ".txt", difdict, vocabulary)
                topics_dif.append(total_dif)

    sorted_indices = sorted(range(len(topics_dif)), \
        key  = lambda k: topics_dif[k])

    sorted_list = sorted(topics_dif)

    printstr = ""
    for i in range(len(sorted_list)):
        printstr += "Topic #" + str(sorted_indices[i]) + \
            " with diff = " + str(sorted_list[i]) + "\n"
    
    with open(outpath + "comparison.summary.txt", "w") as out:
        out.write(printstr)
