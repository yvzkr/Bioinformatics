import re
from collections import Counter
import matplotlib.pyplot as plt

with open("coli.fasta") as f:
    fasta = f.read()
for genome in fasta.split(">")[1:]:
    header, genomeseq = genome.splitlines()[0], "".join(genome.splitlines()[1:])
    counts = Counter(genomeseq)
    genomeSeqlen=0
    genomeSeqlen=counts["A"]+counts["T"]+counts["G"]+counts["C"]


    #print("Counts for the genome:", header)
    #print("A:", counts["A"])
    #print("T:", counts["T"])
    #print("G:", counts["G"])
    #print("C:", counts["C"])
#print(genomeseq)

def Draw_graphic(liste):
    plt.plot(range(0,len(liste)),liste)
    plt.show()

def c_gc_skewness(pieceSeqLen):
    #counts = Counter(genomeseq)
    listey=[0]
    for i in range(0,genomeSeqlen,pieceSeqLen):
        genome=genomeseq[i:i+pieceSeqLen]
        countsGenome=Counter(genome)
        G,C=countsGenome["G"],countsGenome["C"]
        try:
            sGC=(G-C)/(G+C)
        except ZeroDivisionError:
            sGC=0
            #print("sGC:",sGC,"son eleman",listey[-1])
            #print(genome," G nin sayisi= ",G," C nin sayisi= ",C,"gc kaymasi: ",sGC)
        listey.append((listey[-1]+sGC))

        #print(genome," G nin sayisi= ",G," C nin sayisi= ",C,"gc kaymasi: ",sGC)
    Draw_graphic(listey)






c_gc_skewness(50)
