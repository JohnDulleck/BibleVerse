# Extract.py

import sys
import pickle

text = []

# Extracts each verse from its source and converts the 2 line format to single line
def Extract(inputFile):
    with open(inputFile) as fi:
        lines = fi.readlines()
        
    print "Length: ", len(lines)
    
    wordsKjv = {}
        
    for lineIdx in range(0, len(lines), 2):
        text.append(lines[lineIdx].strip('$ \n') + ' ' +  lines[lineIdx + 1].strip())
        wordsLine = lines[lineIdx + 1].strip().split()
        for word in wordsLine:
            if word not in wordsKjv:
                w = word.strip("[].,:;>")
                wordsKjv[w] = w
        

    for i in range(10):
        print text[i]
        
    with open("out.txt", mode='w') as wf:
        wf.writelines(text)
        for line in text:
            wf.writelines(line.strip('$ ') + "\n")
            
    #dc = {"wer":1, "sdf":"erw", "zxc":3}
    #with open("dc.txt", mode='w') as wf:
        #pickle.dump(dc, wf)
        
    #with open("dc.txt", mode='r') as rf:
        #dcr = pickle.load(rf)
        
    k = wordsKjv.keys()
    for i in range(10):
        print k[i]
    return

def CreateDict(inputFile):
    with open('out.txt') as fi:
        lines = fi.readlines()
        
    print "Length: ", len(lines)
    
    wordsKjv = {}
        
    for lineIdx in range(0, len(lines), 2):
        text.append(lines[lineIdx].strip('$ \n') + ' ' +  lines[lineIdx + 1].strip())
        wordsLine = lines[lineIdx + 1].strip().split()
        for word in wordsLine:
            if word not in wordsKjv:
                w = word.strip("[].,:;>")
                wordsKjv[w] = w
        

    for i in range(10):
        print text[i]
        
    with open("out.txt", mode='w') as wf:
        wf.writelines(text)
        for line in text:
            wf.writelines(line.strip('$ ') + "\n")
            
    #dc = {"wer":1, "sdf":"erw", "zxc":3}
    #with open("dc.txt", mode='w') as wf:
        #pickle.dump(dc, wf)
        
    #with open("dc.txt", mode='r') as rf:
        #dcr = pickle.load(rf)
        
    k = wordsKjv.keys()
    for i in range(10):
        print k[i]
    return

if __name__ == "__main__":
    Extract (sys.argv[1])