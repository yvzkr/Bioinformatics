import re
import matplotlib.pyplot as plt
import collection


sequence=""
uzunluk=0
with open("pEGFP.fasta", "r") as f:
    header=f.readline()
    veri=f.read()
    for harf in veri:
        nesne=re.search("\\n",harf)
        if nesne:
            pass
        else:
            uzunluk=uzunluk+1
            sequence=sequence+harf

#print(uzunluk,"\n",header)

def GCKaymasi():
    #print(sequence,"   ", uzunluk)
    #uzunluk=100
    aralık=10
    baslangic=0
    adet=0
    topsGC,topsATc=0.0000,0.00000
    listex,listey=[],[]
    for i in range(baslangic,uzunluk,aralık):
        #print(sequence[i:aralık+i])
        adet=adet+1
        blok=sequence[i:aralık+i]
        #print("blok da yazan",blok)
        #sGC hesaplama

        A,T,G,C=0,0,0,0
        for a in blok:
            if a=="G":
                G=G+1
            elif a=="C":
                C=C+1
        #print("A : {}\n T : {}\n G : {}\n C : {}\n ".format(A,T,G,C))

        try:
            sGC=(float)(G-C)/(G+C)
            #sAT=(float)(A-T)/(A+T)
        except ZeroDivisionError:
            sGC=0

        #print("sonuçlar",sGC)

        topsGC=topsGC+sGC
        listex=listex+[adet]
        listey=listey+[topsGC]
    ######
    grafikciz(adet,listex,listey)


def ATKaymasi():
    #print(sequence,"   ", uzunluk)
    #uzunluk=100
    aralık=50
    baslangic=0
    adet=0
    topsAT=0.00000
    listex,listey=[],[]
    for i in range(baslangic,uzunluk,aralık):
        #print(sequence[i:aralık+i])
        adet=adet+1
        blok=sequence[i:aralık+i]
        #print("blok da yazan",blok)
        #sGC hesaplama
        A,T,G,C=0,0,0,0
        for a in blok:
            if a=="A":
                A=A+1
            elif a=="T":
                T=T+1
        #print("A : {}\n T : {}\n G : {}\n C : {}\n ".format(A,T,G,C))

        try:
            #sGC=(float)(G-C)/(G+C)
            sAT=(float)(A-T)/(A+T)
        except ZeroDivisionError:
            sAT=0

        #print("sonuçlar",sAT)

        topsAT=topsAT+sAT
        listex=listex+[adet]
        listey=listey+[topsAT]
    ######
    grafikciz(adet,listex,listey)



def grafikciz(adet,listex,listey):
    #print("GC kayması: ",sGC," AT kayması",sAT,"\n topsGC :",topsGC)
    print(adet,"====",len(sequence))
    plt.plot(listex, listey)#
    #plt.axis([0, 10, 0, 20])
    plt.show()

def CpG():



    #print("A : {}\n T : {}\n G : {}\n C : {}\n ".format(A,T,G,C))
