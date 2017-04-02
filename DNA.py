#-*- coding: utf-8 -*-
from collections import Counter
import matplotlib as mpl
import re
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


class DNA:
    def __init__(self, filename, start=3):
        self.type = "DNA"
        self.header = ""
        self.genomeseq = ""
        self.genome_seq_len=0
        self.start = 3
        self.direction(start)
        self.read_FASTA(filename)

    def read_FASTA(self,filename):
        with open(filename) as f:
            fast = f.read()
            for genome in fast.split(">")[1:]:
                self.header, self.genomeseq = genome.splitlines()[0], "".join(genome.splitlines()[1:])
                self.genome_seq_len = len(self.genomeseq)
        #print(self.genomeseq)

    def direction(self, start):
        if start == 3:
            self.start, self.finish = 3, 5
        elif start == 5:
            self.start, self.finish = 5, 3

            #"""buraya kadar DNA nin sabit olan zellikleri tanimlandi"""

    def c_gc_skewness(self, piece_seq_len=50):
        # counts = Counter(genomeseq)
        liste = [0]
        for i in range(0, self.genome_seq_len, piece_seq_len):
            genome = self.genomeseq[i:i + piece_seq_len]
            countsGenome = Counter(genome)
            G, C = countsGenome["G"], countsGenome["C"]
            try:
                sGC = (G - C) / (G + C)
            except ZeroDivisionError:
                sGC = 0
                # print("sGC:",sGC,"son eleman",listey[-1])
                # print(genome," G nin sayisi= ",G," C nin sayisi= ",C,"gc kaymasi: ",sGC)
            liste.append((liste[-1] + sGC))
            # print(genome," G nin sayisi= ",G," C nin sayisi= ",C,"gc kaymasi: ",sGC)
        plt.plot(range(0, len(liste)), liste)
        plt.show()

    def c_at_skewness(self, piece_seq_len=50):
        # counts = Counter(genomeseq)
        liste = [0]
        for i in range(0, self.genome_seq_len, piece_seq_len):
            genome = self.genomeseq[i:i + piece_seq_len]
            countsGenome = Counter(genome)
            A, T = countsGenome["A"], countsGenome["T"]
            try:
                sAT = (A - T) / (A + T)
            except ZeroDivisionError:
                sAT = 0
                # print("sGC:",sGC,"son eleman",listey[-1])
                # print(genome," G nin sayisi= ",G," C nin sayisi= ",C,"gc kaymasi: ",sGC)
            liste.append((liste[-1] + sAT))
            # print(genome," G nin sayisi= ",G," C nin sayisi= ",C,"gc kaymasi: ",sGC)

        plt.plot(range(0, len(liste)), liste)
        plt.show()

    def CpG_func(self, pieceSeqLen=50):
        liste = []
        for i in range(0, self.genome_seq_len, pieceSeqLen):
            genome = self.genomeseq[i:i + pieceSeqLen]  # belirledigimiz genom araligini aldik
            countsGenome = Counter(genome)  # C ve G yi saymak için countsGenome
            C, G = countsGenome["C"], countsGenome["G"]  # C ve G yi saydık Counter ile
            CG = len(re.findall("CG", genome))  # regex ile CG birleşkesini bulduk
            try:
                CpG = CG / (C * G)  # CpG yi hesapladık
            except ZeroDivisionError:
                CpG = 0
            print("Genome {}\nbölüme sayisi {}\nCnin sayisi {}\nGnin sayisi: {}".format(genome,CpG,C,G))
            liste.append(CpG)
        plt.plot(range(0, len(liste)), liste)
        plt.show()

        # print(genome)
        # print("CG birlikteliginin sayisi: ", CG)
        # print("C lerin sayisi: ",C," G lerin sayisi: ",G)
        # print("Sonuc: ",CpG)

    def Zcurved(self):
        listx, listy, listz = [], [], []
        A, T, G, C = 0, 0, 0, 0
        # sayac=0
        for i in self.genomeseq:
            if i == "A":
                A = A + 1
            elif i == "T":
                T = T + 1
            elif i == "G":
                G = G + 1
            elif i == "C":
                C = C + 1
            """sayac=sayac+1
            if sayac==10:
                break"""
            listx.append((A + G) - (C + T))
            listy.append((A + C) - (G + T))
            listz.append((A + T) - (G + C))
            # bunlar üç boyutlu bir grafikte çizilecek
        mpl.rcParams['legend.fontsize'] = 10
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot(listx, listy, listz)


        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        ax.legend()
        plt.show()
        # print("A nın sayısı: {}\nT nin sayisi: {}\nG nin sayisi: {}\nC nin sayisi: {}".format(A,T,G,C))
        # print(listx)

    def shannas_entropi(self):
        pass

    def de_burjin(self):
        pass



        #print(liste)

def dizi_hizalama(dizi1,dizi2):
    liste=[[]]
    deger=0
    for i in range(0,10):
        #liste[0][0]=0
        deger=deger-2
    deger=0
    for i in range(0,len(dizi2)):
        #liste[j][0]=deger
        deger=deger-2
    print(liste)






#eren = DNA("pEGFP.fasta")
coli = DNA("coli.fasta")

#eren.de_burjin()
