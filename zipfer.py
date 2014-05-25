import string
import collections
from pprint import pprint
from matplotlib import pyplot


def process_file(filename):
    hist={}
    myfile=open(filename)
    for line in myfile:
        process_line(line, hist)
    return hist
    
    
def process_line(line, hist):
    line=line.replace("-"," ")
    for word in line.split():
    
        word = word.strip(string.punctuation + string.whitespace)
        word=word.lower()
        
        if word in hist:
            hist[word]+=1
        else:
            hist[word]=1
            
            
def print_ranks_save_data(hist):
    # sort the hist dictionary
    hist = sorted(hist.items(), key=lambda x:x[1],reverse=True)
    
    # write data to file
    results = open("results.txt","w")

    for k,v in hist:
        results.write("%s %s %d\n" % (k,' '*(15-len(k)),v))
    
    results.close()
    # print rank vs frequency
    histlist = []
    for i, (k,v) in enumerate(hist):
        histlist.append((i+1,v))
        
    return histlist
    
def plot_ranks(histlist, scale="log"):
    rank,frequency = zip(*histlist)
    pyplot.clf()
    pyplot.xscale(scale)
    pyplot.yscale(scale)
    pyplot.title("Zipfer's law plot")
    pyplot.xlabel("rank")
    pyplot.ylabel("frequency")
    pyplot.plot(rank, frequency, "b.-")
    pyplot.grid()
    pyplot.show()
    

def main():
    filename="emma.txt"
    hist=process_file(filename)
    histlist = print_ranks_save_data(hist)
    pprint(histlist)
    plot_ranks(histlist, scale="log")
    
main()


