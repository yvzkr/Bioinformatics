#-*- coding: cp1254 -*-
from collections import Counter
import matplotlib as mpl
import re
from numpy import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math


class DNA(QtCore.QThread):
    def __init__(self, filename, start=3):
        QtCore.QThread.__init__(self)
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


    def direction(self, start):
        if start == 3:
            self.start, self.finish = 3, 5
        elif start == 5:
            self.start, self.finish = 5, 3


    def c_gc_skewness(self, piece_seq_len=50):


        self.val='asdsadasd'
        self.emit(QtCore.SIGNAL("dogruGiris(QString)"), self.val)
        liste = [0]
        for i in range(0, self.genome_seq_len, piece_seq_len):
            genome = self.genomeseq[i:i + piece_seq_len]
            countsGenome = Counter(genome)
            G, C = countsGenome["G"], countsGenome["C"]
            try:
                sGC = (G - C) / (G + C)
            except ZeroDivisionError:
                sGC = 0
            liste.append((liste[-1] + sGC))
        fig1=plt
        fig1.figure("C_GC_Skewness")
        fig1.plot(range(0, len(liste)), liste)


    def c_at_skewness(self, piece_seq_len=50):

        liste = [0]
        for i in range(0, self.genome_seq_len, piece_seq_len):
            genome = self.genomeseq[i:i + piece_seq_len]
            countsGenome = Counter(genome)
            A, T = countsGenome["A"], countsGenome["T"]
            try:
                sAT = (A - T) / (A + T)
            except ZeroDivisionError:
                sAT = 0
            liste.append((liste[-1] + sAT))

        fig2 = plt
        fig2.figure("C_AT_Skewness")
        fig2.plot(range(0, len(liste)), liste)


    def CpG_func(self, pieceSeqLen=50):
        liste = []
        for i in range(0, self.genome_seq_len, pieceSeqLen):
            genome = self.genomeseq[i:i + pieceSeqLen]  # belirledigimiz genom araligini aldik
            countsGenome = Counter(genome)  # C ve G yi saymak için countsGenome
            C, G = countsGenome["C"], countsGenome["G"]  # C ve G yi saydık Counter ile
            CG = len(re.findall("CG", genome))  # regex ile CG birleşkesini bulduk
            try:
                CpG = CG * pieceSeqLen / (C * G)  # CpG yi hesapladık
            except ZeroDivisionError:
                CpG = 0
            print("Genome {}\nbölüme sayisi {}\nCnin sayisi {}\nGnin sayisi: {}".format(genome,CpG,C,G))
            liste.append(CpG)
        fig3=plt
        fig3.figure("CpG")
        fig3.plot(range(0, len(liste)), liste)

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
        mpl.rcParams['legend.fontsize'] = 10
        fig4 = plt
        fig4.figure("ZCurved")
        ax = fig4.gca(projection='3d')
        ax.plot(listx, listy, listz)


        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        ax.legend()

    def de_burjin(self):
        pass

    def dizi_hizalama(self,dizi1,dizi2):

        self.matris=zeros((len(dizi1)+1,len(dizi2)+1))
        self.deger               =   0

        for i in range(0,len(dizi2)+1):
            self.matris[0][i]        =   self.deger
            self.deger               =   self.deger - 2
        self.deger                   =   0

        for i in range(0,len(dizi1)+1):
            self.matris[i][0]        =   self.deger
            self.deger               =   self.deger - 2

        #for i in self.matris:
        #    print(i)

        self.dikeyeksen          =   ["X"]
        self.yatayeksen          =   ["X"]
        for i in dizi1:
            self.dikeyeksen.append(i)
        for i in dizi2:
            self.yatayeksen.append(i)

        #print(self.yatayeksen)
        self.gep=-2
        self.match=5
        self.Mismatch=-5
        #print(len(self.dikeyeksen))
        for i in range(1,len(self.yatayeksen)):
            for j in range(1,len(self.dikeyeksen)):
                if self.dikeyeksen[j]    ==  self.yatayeksen[i]:
                    #print("Bunlarin ikisi: ",self.dikeyeksen[j]," ",self.yatayeksen[i])
                    self.matris[j][i]    =   self.matris[j-1][i-1]    +   5
                else:
                    self.solust          =   self.matris[j-1][i-1]    +   self.Mismatch
                    self.ust             =   self.matris[j-1][i]      +   self.gep
                    self.sol             =   self.matris[j][i-1]      +   self.gep
                    if self.solust>self.ust and self.solust>self.sol:
                        self.matris[j][i]    =   self.solust
                    elif self.ust>self.solust and self.ust>self.sol:
                        self.matris[j][i]    =   self.ust
                    else:
                        self.matris[j][i]    =   self.sol

        return self.matris


    def shannas_entropi(self,sequence):
        print ("Class i�indeki shannas i�erisindeyim")
        counts=Counter(sequence)
        self.A=float(counts["A"])
        self.T=float(counts["T"])
        self.G=float(counts["G"])
        self.C=float(counts["C"])

        try:
            if self.A !=0.0:
                self.A       =   (self.A/len(sequence))*(math.fabs(math.log(2,(self.A/len(sequence)/(1/4)))))

            if self.T !=0.0:
                self.T       =   (self.T/len(sequence))*(math.fabs(math.log(2,(self.T/len(sequence)/(1/4)))))

            if self.G !=0.0:
                self.G       =   (self.G/len(sequence))*(math.fabs(math.log(2,(self.G/len(sequence)/(1/4)))))

            if self.C !=0.0:
                self.C       =   (self.C/len(sequence))*(math.fabs(math.log(2,(self.C/len(sequence)/(1/4)))))

        except ZeroDivisionError:
            self.A       =   0.0
            self.G       =   0.0
            self.T       =   0.0
            self.C       =   0.0
        self.shanna      =   float(self.A +  self.T)
        return self.shanna

def dizi_hizalama(dizi1,dizi2):
    matris=zeros((len(dizi1)+1,len(dizi2)+1))
    deger               =   0

    for i in range(0,len(dizi2)+1):
        matris[0][i]        =   deger
        deger               =   deger - 2
    deger                   =   0

    for i in range(0,len(dizi1)+1):
        matris[i][0]        =   deger
        deger               =   deger - 2

    for i in matris:
        print(i)

    dikeyeksen          =   ["X"]
    yatayeksen          =   ["X"]
    for i in dizi1:
        dikeyeksen.append(i)
    for i in dizi2:
        yatayeksen.append(i)

    print(yatayeksen)
    gep=-2
    match=5
    Mismatch=-5

    for i in range(1,len(yatayeksen)):
        for j in range(1,len(dikeyeksen)):
            if dikeyeksen[j]    ==  yatayeksen[i]:
                matris[j][i]    =   matris[j-1][i-1]    +   5
            else:
                solust          =   matris[j-1][i-1]    +   Mismatch
                ust             =   matris[j-1][i]      +   gep
                sol             =   matris[j][i-1]      +   gep
                if solust>ust and solust>sol:
                    matris[j][i]    =   solust
                elif ust>solust and ust>sol:
                    matris[j][i]    =   ust
                else:
                    matris[j][i]    =   sol


    for i in matris:
        print(i)



def shannas_entropi(sequence):
    counts=Counter(sequence)
    A,T,G,C=counts["A"],counts["T"],counts["G"],counts["C"]
    try:
        A       =   (A/len(sequence))*(math.log(2,(A/len(sequence)/(1/4))))
        T       =   (T/len(sequence))*(math.log(2,(T/len(sequence)/(1/4))))
        G       =   (G/len(sequence))*(math.log(2,(G/len(sequence)/(1/4))))
        C       =   (C/len(sequence))*(math.log(2,(C/len(sequence)/(1/4))))
    except ZeroDivisionError:
        A       =   0
        G       =   0
        T       =   0
        C       =   0
    shanna      =   A +  T
    return shanna



#coli = DNA("coli.fasta")
#coli.c_at_skewness()
#coli.c_gc_skewness()
#coli.CpG_func()
#coli.Zcurved()
#dizi_hizalama("TCCGCAT","ATGCCAGCAT")
#eren.de_burjin()
#coli.dizi_hizalama("TCCGCAT","ATGCCAGCAT")
#coli.shannas_entropi("GCGCGCG")
