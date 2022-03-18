
import re
def tokenize(lines):
    return re.sub("[^\w]", " ",lines).split() 
    
