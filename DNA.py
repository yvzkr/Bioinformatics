import re


bazlar=""
uzunluk=0
with open("sequence.fasta", "r") as f:
    f.readline()
    veri=f.read()
    for harf in veri:
        nesne=re.search("\\n",harf)
        if nesne:
            pass
        else:
            uzunluk=uzunluk+1
            bazlar=bazlar+harf


#print(bazlar,"   ", uzunluk)
uzunluk=35
aralık=5
baslangic=0
start=0

for i in range(baslangic,uzunluk,aralık):
    print(bazlar[i:aralık+i])
    blok=bazlar[i:aralık+i]
    print("blok da yazan",blok)
    #sGC hesaplama
    A,T,G,C=0,0,0,0
    for a in blok:
        if a=="A":
            A=A+1
        elif a=="T":
            T=T+1
        elif a=="G":
            G=G+1
        elif a=="C":
            C=C+1
    print("A : {}\n T : {}\n G : {}\n C : {}\n ".format(A,T,G,C))
    try:
        sGC=(float)(G-C)/(G+C)
        sAT=(float)(A-T)/(A+T)
    except ZeroDivisionError:
        sGC=0.0
        sAT=0.0

    print("GC kayması: ",sGC," AT kayması",sAT)





#print("A : {}\n T : {}\n G : {}\n C : {}\n ".format(A,T,G,C))
