#-*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arayuz.ui'
#
# Created: Fri May 19 15:32:17 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
from PyQt4.QtCore import pyqtSignal
from PyQt4 import QtCore, QtGui
from arkaPlan import Thread
import time



from DNA import DNA
import matplotlib.pyplot as plt
import sys
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dna(QtGui.QWidget):
    clicked = pyqtSignal()
    girdi =pyqtSignal()
    def __init__(self,parent=None):
        super(Ui_Dna, self).__init__(parent)
        self.fileName = ''
        self.gcSkew   = ''
        self.cPG      = ''
        self.zCurved  = ''
        self.atSkew   = ''

        self.etiket_yukleniyor="Yükleniyor.. Lütfen Bekleyiniz"
        self.setupUi(self)
        self.c_at_skewness.clicked.connect(self.slot_cATSkew_clicked)
        self.c_gc_skewness.clicked.connect(self.slot_cGCSkew_clicked)
        self.cpg.clicked.connect(self.slot_cPG_clicked)
        self.z_curved.clicked.connect(self.slot_zCurved_clicked)
        self.dosya_secim_butonu.clicked.connect(self.fileOpen)
        self.entropi_butonu.clicked.connect(self.entropiHesapla)
        self.dizi_hizala_butonu.clicked.connect(self.diziHizala)
        self.clicked.connect(self.etiketDegistir)
        self.grafik_cizme_butonu.clicked.connect(self.cizFunction)


    def dogruGiris(self,yuklendi):

        self.secili_file_etiketi.setText(_translate("Dna", "{0}".format(yuklendi), None))
        time.sleep(1)
        self.arkaPlan.plt
        self.arkaPlan.terminate()
        print(self.arkaPlan.terminate())
        self.arkaPlan.cikis()



    def slot_cATSkew_clicked(self, checked):
        # prints the emitted signal in 'edt_output'
        self.atSkew=checked

    def slot_cGCSkew_clicked(self,checked):
        self.gcSkew=checked

    def slot_cPG_clicked(self,checked):
        self.cPG=checked

    def slot_zCurved_clicked(self,checked):
        self.zCurved=checked


    def etiketDegistir(self):
        self.secili_file_etiketi.setText("")
        #print (type(self.fileName))
        self.parcalanmis = self.fileName.split("/")
        #print (self.parcalanmis)
        self.secili_file_etiketi.setText(_translate("Dna", "Eklenen->{0}".format(self.parcalanmis[-1]), None))

    def cizFunction(self):
        #print (self.fileName)
        self.secili_file_etiketi.setText(_translate("Dna", "Yukleniyor", None))
        self.arkaPlan = Thread(None, self.fileName, self.atSkew, self.gcSkew, self.cPG, self.zCurved)
        self.connect(self.arkaPlan, QtCore.SIGNAL("dogruGiris(QString)"), self.dogruGiris)
        self.arkaPlan.baslat()

    def diziHizala(self):
        self.hizalanacak=''
        self.ilk_dizi = str(self.ilk_dizi_girisi.text())
        self.ikinci_dizi = str(self.ikinci_dizi_girisi.text())
        self.testDNA = DNA(self.fileName)
        self.sonuc = (self.testDNA.dizi_hizalama(self.ilk_dizi,self.ikinci_dizi))
        self.sonuc.tolist()

        for i in self.sonuc:
            self.hizalanacak += str('{0}\n'.format(i))

        self.arayuz_text.setText(self.hizalanacak)

    def entropiHesapla(self):
        self.first_array=str(self.shannas_entropi_girisi.text())
        self.testDNA=DNA(self.fileName)
        self.sonuc=str(self.testDNA.shannas_entropi(self.first_array))
        self.arayuz_text.setText(self.sonuc)
        print(self.sonuc)

        #self.gcSkew = self.c_gc_skewness.isChecked()
        #self.cPG = self.cpg.isChecked()
        #self.zCurved = self.z_curved.isChecked()
        #self.atSkew = self.c_at_skewness.isChecked()
        #self.dnaOlustur = DNA(self.fileName)
        #if self.gcSkew == True:
        #    self.dnaOlustur.c_gc_skewness()
        #if self.cPG == True:
        #    self.dnaOlustur.CpG_func()
        #if self.zCurved == True:
        #    self.dnaOlustur.Zcurved()
        #if self.atSkew == True:
        #    self.dnaOlustur.c_at_skewness()


    def fileOpen(self, Dna):
        self.fileName = QtGui.QFileDialog.getOpenFileName(self, 'OpenFile')
        #print (self.fileName)
        self.clicked.emit()

    def setupUi(self, Dna):
        Dna.resize(960, 800)
        self.dosya_secim_butonu = QtGui.QPushButton(Dna)
        self.dosya_secim_butonu.setGeometry(QtCore.QRect(80, 120, 111, 91))
        self.dosya_secim_butonu.setObjectName(_fromUtf8("dosya_secim_butonu"))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.secili_file_etiketi = QtGui.QLabel(Dna)
        self.secili_file_etiketi.setGeometry(QtCore.QRect(50, 80, 260, 31))
        self.secili_file_etiketi.setFont(font)
        self.secili_file_etiketi.setAlignment(QtCore.Qt.AlignCenter)
        self.secili_file_etiketi.setObjectName(_fromUtf8("secili_file_etiketi"))
        self.ilk_dizi_girisi = QtGui.QLineEdit(Dna)
        self.ilk_dizi_girisi.setGeometry(QtCore.QRect(440, 50, 441, 27))
        self.ilk_dizi_girisi.setObjectName(_fromUtf8("ilk_dizi_girisi"))
        self.ikinci_dizi_girisi = QtGui.QLineEdit(Dna)
        self.ikinci_dizi_girisi.setGeometry(QtCore.QRect(440, 100, 441, 27))
        self.ikinci_dizi_girisi.setObjectName(_fromUtf8("ikinci_dizi_girisi"))
        self.ilk_dizi_etiketi = QtGui.QLabel(Dna)
        self.ilk_dizi_etiketi.setGeometry(QtCore.QRect(440, 20, 221, 17))
        self.ilk_dizi_etiketi.setObjectName(_fromUtf8("ilk_dizi_etiketi"))
        self.ikinci_dizi_etiketi = QtGui.QLabel(Dna)
        self.ikinci_dizi_etiketi.setGeometry(QtCore.QRect(440, 80, 221, 17))
        self.ikinci_dizi_etiketi.setObjectName(_fromUtf8("ikinci_dizi_etiketi"))
        self.arayuz_text = QtGui.QTextBrowser(Dna)
        self.arayuz_text.setGeometry(QtCore.QRect(80, 310, 800, 400))
        self.arayuz_text.setObjectName(_fromUtf8("arayuz_text"))
        self.arayuz_text.setFontPointSize(25)

        self.c_gc_skewness = QtGui.QCheckBox(Dna)
        self.c_gc_skewness.setGeometry(QtCore.QRect(80, 240, 121, 22))
        self.c_gc_skewness.setObjectName(_fromUtf8("c_gc_skewness"))
        self.cpg = QtGui.QCheckBox(Dna)
        self.cpg.setGeometry(QtCore.QRect(80, 220, 88, 22))
        self.cpg.setObjectName(_fromUtf8("cpg"))
        self.z_curved = QtGui.QCheckBox(Dna)
        self.z_curved.setGeometry(QtCore.QRect(80, 280, 88, 22))
        self.z_curved.setObjectName(_fromUtf8("z_curved"))
        self.c_at_skewness = QtGui.QCheckBox(Dna)
        self.c_at_skewness.setGeometry(QtCore.QRect(80, 260, 131, 22))
        self.c_at_skewness.setObjectName(_fromUtf8("c_at_skewness"))

        self.shannas_entropi_etiketi = QtGui.QLabel(Dna)
        self.shannas_entropi_etiketi.setGeometry(QtCore.QRect(440, 140, 101, 17))
        self.shannas_entropi_etiketi.setObjectName(_fromUtf8("shannas_entropi_etiketi"))
        self.shannas_entropi_girisi = QtGui.QLineEdit(Dna)
        self.shannas_entropi_girisi.setGeometry(QtCore.QRect(440, 160, 441, 27))
        self.shannas_entropi_girisi.setObjectName(_fromUtf8("shannas_entropi_girisi"))

        self.entropi_butonu = QtGui.QPushButton(Dna)
        self.entropi_butonu.setGeometry(QtCore.QRect(770, 240, 111, 60))
        self.entropi_butonu.setObjectName(_fromUtf8("entropi_butonu"))

        self.dizi_hizala_butonu = QtGui.QPushButton(Dna)
        self.dizi_hizala_butonu.setGeometry(QtCore.QRect(600, 240, 71, 60))
        self.dizi_hizala_butonu.setObjectName(_fromUtf8("dizi_hizala_butonu"))

        self.grafik_cizme_butonu = QtGui.QPushButton(Dna)
        self.grafik_cizme_butonu.setGeometry(QtCore.QRect(440, 240, 71, 60))
        self.grafik_cizme_butonu.setObjectName(_fromUtf8("grafik_cizme_butonu"))

        self.retranslateUi(Dna)
        QtCore.QMetaObject.connectSlotsByName(Dna)

    def retranslateUi(self, Dna):
        Dna.setWindowTitle(_translate("Dna", "Form", None))
        self.dosya_secim_butonu.setText(_translate("Dna", "Dosya Seç", None))
        self.secili_file_etiketi.setText(_translate("Dna", "Seçili Dosya Bulunamadı", None))
        self.ilk_dizi_etiketi.setText(_translate("Dna", "Hizalanacak İşlemi Yapılacak İlk Dizi", None))
        self.ikinci_dizi_etiketi.setText(_translate("Dna", "Hizalanacak İşlemi Yapılacak İkinci Dizi", None))
        self.c_gc_skewness.setText(_translate("Dna", "C_GC_Skewness", None))
        self.cpg.setText(_translate("Dna", "CpG", None))
        self.z_curved.setText(_translate("Dna", "Z Curved", None))
        self.c_at_skewness.setText(_translate("Dna", "C_AT_Skewness", None))
        self.shannas_entropi_etiketi.setText(_translate("Dna", "Shannas_Entropi", None))
        self.dizi_hizala_butonu.setText(_translate("Dna", "Dizi Hizala", None))
        self.entropi_butonu.setText(_translate("Dna", "Entropi Hesapla", None))
        self.grafik_cizme_butonu.setText(_translate("Dna", "Grafik Çiz", None))


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Ui_Dna()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
