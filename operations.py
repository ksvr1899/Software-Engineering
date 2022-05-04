"""Extension of Strings and words """
import re
import nltk


# tokenizing the entire data
def tokenize(lines):
    return re.sub(r" [^\w] ", " ", lines).split()


# counting the words
def count(words):
    return nltk.FreqDist(words)


# word replacment in the file
def replaceword(file_x, searchword, repword):
    """Repalcing the word in the file"""
    with open(file_x, 'r') as file:
        filedata = file.read()
    split_list = re.split(" ", filedata)
    # splitting the text utilizing spaces into a rundown
    for i in range(len(split_list)):
        if searchword == split_list[i]:
            split_list[i] = repword
    filedata = " ".join(split_list)
    # Writing the replaced data in our
    # text file
    with open(file_x, 'w') as file:
        file.write(filedata)
    print("text Replaced done")  # printing the new string


# grep function
def grepline(file_x, grep_word):
    """Grep line Function"""
    split_list = []
    grep_lines = []
    with open(file_x, 'r') as file:
        filedata = file.readlines()

    for i in filedata:
        split_list = i.split()
        if grep_word in split_list:
            grep_lines.append(i)
    return grep_lines
