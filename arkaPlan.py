#-*- coding: cp1254 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from DNA import DNA
import matplotlib.pyplot as plt
class Thread(QThread):
    update=pyqtSignal(str)

    def __init__(self,parent=None,fileName='',atSkew='',gcSkew='',cPG='', zCurved=''):
        super(Thread, self).__init__(parent)
        self.count=0
        self.test=''
        self.atSkew     = atSkew
        self.gcSkew     = gcSkew
        self.cPG        = cPG
        self.zCurved    = zCurved
        self.fileName   = fileName
        self.plt=plt

    def cikis(self):
        #self.destroyed()
        self.quit()

    def baslat(self):
        self.start()

    def run(self):
        self.dnaOlustur = DNA(self.fileName)
        if self.gcSkew == True:
            self.dnaOlustur.c_gc_skewness()
        if self.cPG == True:
            self.dnaOlustur.CpG_func()
        if self.zCurved == True:
            self.dnaOlustur.Zcurved()
            print ("baba Zcurveddddddddddddddd"+type(self.dnaOlustur.Zcurved()))
        if self.atSkew == True:
            self.dnaOlustur.c_at_skewness()
        self.test = "Yeni İşleme Hazir"
        self.plt=plt.show(block=True)

        self.emit(QtCore.SIGNAL("dogruGiris(QString)"), self.test)
