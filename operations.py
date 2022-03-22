import re
import nltk


def tokenize(lines):
    return re.sub("[^\w]", " ",lines).split()

def count(words):
    return nltk.FreqDist(words)



# Read in the file
def replaceword(x,searchword,replaceword):
    
    with open(x, 'r') as file :
      filedata = file.read()
    
    split_list = re.split(" ",filedata) #splitting the text utilizing spaces into a rundown
    print(split_list)
    i=0
    for i in range(len(split_list)):
        if searchword == split_list[i]:
            split_list[i]=replaceword
            print(split_list[i])
    print(split_list)
            
    filedata=" ".join(split_list)
        
    
    # Writing the replaced data in our
    # text file
    with open(x, 'w') as file:
  
        file.write(filedata)

    print("text Replaced done") #printing the new string




