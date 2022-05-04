"""Strings and Words Operations"""
#Download punkt resource
#nltk.download('punkt')
import operations

# Input document
data=input("Enter the file name to be processed: ")
#reading the file
with open(data) as f:
    lines = f.readlines()
words=[]
for x in lines:
    # Tokenize the text string and storing in the list
    words= words + operations.tokenize(x)
# Frequency distribution of the words using nltk
fdist= operations.count(words)
# Creating a dictionary of the words and their frequency used
filtered_word_freq = dict((word, freq) for word, freq in fdist.items() if not word.isdigit())
# Printing the count of frequency of each unique word.
print("\nUnique Words in the file with their frequency:\n")
for key, value in filtered_word_freq.items():
    print(key, ' : ', value)
#...................................................
#Second Requirement

word=input("\nEnter the word to search for:")
replace_word=input("\nEnter the word to Replace it with:")

operations.replaceword(data,word,replace_word)

#.....................................................
#third requirement
#implementing grepline function

grep_word=input("\nEnter the word name to search: ")
grep_file=input("\nEnter the file name:")
grep_lines=[]
#lines will be stored in the list grep_lines
grep_lines=operations.grepline(grep_file,grep_word)
#checking the output
print(grep_lines)
