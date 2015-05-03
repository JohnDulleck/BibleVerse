# Extract.py

import sys
import pickle

text = []

# Extracts each verse from its source and converts the 2 line format to single line
def Extract(inputFile):
    with open(inputFile) as fi:
        lines = fi.readlines()
        
    print "Length: ", len(lines)
    
    references = {}
    verses = {}
        
    # Each verse occupies 2 lines, the first line is the verse reverence,
    # the second line is the verse text
    for lineIdx in range(0, len(lines), 2):
        # The verse reference is the key, the verse text is the value
        verses[lines[lineIdx].strip('$ \n')] = lines[lineIdx + 1].strip('\n ')
        
    for verse in verses.keys():         # for each verse
        words = verses[verse].split()   # Split into words
        
        for word in words:
            w = word.strip("[].,:;>")   # Remove all formatting
            
            if 4 > len(w):              # Only 4 letters or longer
                continue
            
            if w not in references:     # For each word, create a dictionary key
                references[w] = []
                
            references[w].append(verse) # and then add a reference for each verse 
                                        # that contains the word
    
    with open("versepickle.txt", mode='w') as wf:   # Store the verses dictionary
        pickle.dump(verses, wf)
        
    with open("refpickle.txt", mode='w') as wf:     # Store the references dictionary
        pickle.dump(references, wf)    
        
def GetVerses(word):
    with open("refpickle.txt", mode='r') as rf:     # Read the references dictionary
        references = pickle.load(rf)      
        
    with open("versepickle.txt", mode='r') as rf:   # Read the verses dictionary
        verses = pickle.load(rf)    
        
    try:
        refs = references[word]
    except KeyError:
        print "No references found for '%s'" % word
        return
    for ref in refs:
        print ref + ' ' + verses[ref]

if __name__ == "__main__":
    # Extract (sys.argv[1])
    GetVerses(sys.argv[1])