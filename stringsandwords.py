# Download punkt resource
#nltk.download('punkt')


import tokens
import count

# Input document
data=input("Enter the file name to be processed: ")
#reading the file
with open(data) as f:
    lines = f.readlines()
    
words=[]
for x in lines:
    # Tokenize the text string and storing in the list
    words= words + tokens.tokenize(x)

# Frequency distribution of the words using nltk
fdist= count.frequency(words)

# Creating a dictionary of the words and their frequency used
filtered_word_freq = dict((word, freq) for word, freq in fdist.items() if not word.isdigit())

# Printing the count of frequency of each unique word.
print("\nUnique Words in the file with their frequency:\n")
for key, value in filtered_word_freq.items():
    print(key, ' : ', value)