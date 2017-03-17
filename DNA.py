from collections import Counter
import matplotlib.pyplot as plt


class DNA:
    def __init__(self, filename, start=3):
        self.type   =   "DNA"
        self.direction(start)
        self.read_FASTA(filename)


    def read_FASTA(self, filename):
        with open(filename) as f:
            fasta   =   f.read()
        for genome in fasta.split(">")[1:]:
            self.header, self.genomeseq = genome.splitlines()[0], "".join(genome.splitlines()[1:])
            self.genomeSeqlen           = len(self.genomeseq)


    def direction(self, start):
        if start    ==  3:
            self.start,self.finish      =   3,5
        elif start  ==  5:
            self.start,self.finish      =   5,3

            ####buraya kadar DNA nın sabit olan özellikleri tanımlandı
    def c_gc_skewness(self, pieceSeqLen):
        #counts = Counter(genomeseq)
        liste=[0]
        for i in range(0,self.genomeSeqlen,pieceSeqLen):
            genome=self.genomeseq[i:i+pieceSeqLen]
            countsGenome=Counter(genome)
            G,C=countsGenome["G"],countsGenome["C"]
            try:
                sGC=(G-C)/(G+C)
            except ZeroDivisionError:
                sGC=0
                #print("sGC:",sGC,"son eleman",listey[-1])
                #print(genome," G nin sayisi= ",G," C nin sayisi= ",C,"gc kaymasi: ",sGC)
            liste.append((liste[-1]+sGC))
            #print(genome," G nin sayisi= ",G," C nin sayisi= ",C,"gc kaymasi: ",sGC)
        plt.plot(range(0,len(liste)),liste)
        plt.show()

    def c_at_skewness(self, pieceSeqLen):
        #counts = Counter(genomeseq)
        liste=[0]
        for i in range(0,self.genomeSeqlen,pieceSeqLen):
            genome=self.genomeseq[i:i+pieceSeqLen]
            countsGenome    =   Counter(genome)
            A,T             =   countsGenome["A"],countsGenome["T"]
            try:
                sAT=(A-T)/(A+T)
            except ZeroDivisionError:
                sAT=0
                #print("sGC:",sGC,"son eleman",listey[-1])
                #print(genome," G nin sayisi= ",G," C nin sayisi= ",C,"gc kaymasi: ",sGC)
            liste.append((liste[-1]+sAT))
            #print(genome," G nin sayisi= ",G," C nin sayisi= ",C,"gc kaymasi: ",sGC)
        plt.plot(range(0,len(liste)),liste)
        plt.show()




eren    =   DNA("coli.fasta")
coli    =   DNA("coli.fasta")
coli.c_gc_skewness(50)
