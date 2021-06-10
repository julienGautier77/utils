#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sauvegarde automatique de 3 folders dans 3 autres folders avec ajout d  un numero de tir


Created on Fri May  7 11:57:11 2021

@author: juliengautier
"""


try :
    from PyQt5 import uic
except :
    from PyQt4 import uic
    
from pyqtgraph.Qt import QtGui, QtCore
import os, time,sys
import shutil
from pathlib import Path
import pathlib
from os.path import basename

import qdarkstyle
from PyQt5.QtWidgets import QApplication,QVBoxLayout,QHBoxLayout,QWidget,QPushButton,QGridLayout,QSpinBox,QLineEdit,QTextEdit
from PyQt5.QtWidgets import QInputDialog,QSlider,QCheckBox,QLabel,QSizePolicy,QMenu,QMessageBox
from PyQt5.QtWidgets import QShortcut,QDockWidget,QToolBar,QMainWindow,QToolButton,QAction,QStatusBar
from pyqtgraph.Qt import QtCore,QtGui 
from PyQt5.QtCore import Qt,pyqtSlot
from PyQt5.QtGui import QIcon

class MAINSAVE(QMainWindow) :
    
    
    
    
    
    def __init__(self,**kwds):
        
        super().__init__()
        
        p = pathlib.Path(__file__)
        
        sepa=os.sep
        self.icon=str(p.parent) + sepa+'icons' +sepa
        self.setWindowIcon(QIcon(self.icon+'LOA.png'))
        self.setWindowTitle("Save All Files")
        self.config = QtCore.QSettings('confSave.ini', QtCore.QSettings.IniFormat)
        self.waitValue=float(self.config.value("Dossier1"+"/wait"))
        self.path1=self.config.value("Dossier1"+"/path")
        self.pathSave1=self.config.value("Dossier1"+"/pathSave")
        self.path2=self.config.value("Dossier2"+"/path")
        self.pathSave2=self.config.value("Dossier2"+"/pathSave")
        self.path3=self.config.value("Dossier3"+"/path")
        self.pathSave3=self.config.value("Dossier3"+"/pathSave")
        
        self.threadSave=ThreadRunAuto(self)
        self.setup()
        self.actionButton()
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    
    # define button
    def setup(self):
        
        v=QVBoxLayout()
        
        h0=QHBoxLayout()
        labShot=QLabel("shot number:")
        self.nbShot=QSpinBox()
        self.nbShot.setValue(int(self.config.value("Dossier1"+"/nbShot")))
        h0.addWidget(labShot)
        h0.addWidget(self.nbShot)
        
        labWait=QLabel("wait:")
        self.wait=QSpinBox()
        self.wait.setValue(int(self.config.value("Dossier1"+"/wait")))
        h0.addWidget(labWait)
        h0.addWidget(self.wait)
        
        v.addLayout(h0)
        h1=QHBoxLayout()
        self.label1=QPushButton("Path folder 1 : ")
        self.labelPath1=QLineEdit(self.config.value("Dossier1"+"/path"))
        h1.addWidget(self.label1)
        h1.addWidget(self.labelPath1)
        
        self.labelSave1=QPushButton("Save to Path 1 : ")
        
        self.labelPathSave1=QLineEdit(self.config.value("Dossier1"+"/pathSave"))
        
        h1.addWidget(self.labelSave1)
        h1.addWidget(self.labelPathSave1)
        
        v.addLayout(h1)
        
        h2=QHBoxLayout()
        self.label2=QPushButton("Path folder 2 : ")
        self.labelPath2=QLineEdit(self.config.value("Dossier2"+"/path"))
        h2.addWidget(self.label2)
        h2.addWidget(self.labelPath2)
        self.labelSave2=QPushButton("Save to Path 2 : ")
        self.labelPathSave2=QLineEdit(self.config.value("Dossier2"+"/pathSave"))
        h2.addWidget(self.labelSave2)
        h2.addWidget(self.labelPathSave2)
        v.addLayout(h2)
        
        h3=QHBoxLayout()
        self.label3=QPushButton("Path folder 3 : ")
        self.labelPath3=QLineEdit(self.config.value("Dossier3"+"/path"))
        h3.addWidget(self.label3)
        h3.addWidget(self.labelPath3)
        self.labelSave3=QPushButton("Save to Path 3 : ")
        self.labelPathSave3=QLineEdit(self.config.value("Dossier3"+"/pathSave"))
        h3.addWidget(self.labelSave3)
        h3.addWidget(self.labelPathSave3)
        v.addLayout(h3)
        
        Hb=QHBoxLayout()
        self.startButton=QPushButton("Start")
        self.stopButton=QPushButton("Stop")
        Hb.addWidget(self.startButton)
        Hb.addWidget(self.stopButton)
        v.addLayout(Hb)
        
        MainWidget=QWidget()
        
        MainWidget.setLayout(v)
        
        self.setCentralWidget(MainWidget)
    
    def actionButton(self):
        
        self.nbShot.valueChanged.connect(self.setNbShot)
        
        self.wait.valueChanged.connect(self.setWait)
        
        self.label1.clicked.connect(self.actionBrowse1)
        self.labelSave1.clicked.connect(self.actionBrowseSave1)
        self.labelPath1.textChanged.connect(self.pathChange)
        self.labelPathSave1.textChanged.connect(self.pathChange)
        
        self.label2.clicked.connect(self.actionBrowse2)
        self.labelSave2.clicked.connect(self.actionBrowseSave2)
        self.labelPath2.textChanged.connect(self.pathChange)
        self.labelPathSave2.textChanged.connect(self.pathChange)
        
        self.label3.clicked.connect(self.actionBrowse3)
        self.labelSave3.clicked.connect(self.actionBrowseSave3)
        self.labelPath3.textChanged.connect(self.pathChange)
        self.labelPathSave3.textChanged.connect(self.pathChange)
        
        self.startButton.clicked.connect(self.startSave)
        self.stopButton.clicked.connect(self.stopSave)
    
    
    def setWait(self):
        
        self.waitValue=float(self.wait.value())
        self.config.setValue("Dossier1"+"/wait",self.waitValue)
    
    def startSave(self):
        
        self.threadSave.start()
        
    def stopSave(self):
        
        self.threadSave.stopThreadRunAuto()
    
    def setNbShot(self):
        self.nbShotValue=int(self.nbShot.value())
        self.config.setValue("Dossier1"+"/nbShot",self.nbShotValue)
        
    def actionBrowse1(self):
        self.path1=self.config.value("Dossier1"+"/path")
        self.path1=str(QtGui.QFileDialog.getExistingDirectory(self,"Select Directory for Path1 : ",self.path1))
        self.config.setValue("Dossier1"+"/path",self.path1)
        self.labelPath1.setText(self.path1)
        
        
    def actionBrowseSave1(self):
        
        self.pathSave1=self.config.value("Dossier1"+"/pathSave")
        self.pathSave1=str(QtGui.QFileDialog.getExistingDirectory(self,"Select Directory for save Files 1 : ",self.pathSave1))
        self.config.setValue("Dossier1"+"/pathSave",self.pathSave1)
        self.labelPathSave1.setText(self.pathSave1)
    
    def actionBrowse2(self):
        
        self.path2=self.config.value("Dossier2"+"/path")
        self.path2=str(QtGui.QFileDialog.getExistingDirectory(self,"Select Directory for Path2 : ",self.path2))
        self.config.setValue("Dossier2"+"/path",self.path2)
        self.labelPath2.setText(self.path2)
         
    def actionBrowseSave2(self):
        self.pathSave2=self.config.value("Dossier2"+"/pathSave")
        self.pathSave2=str(QtGui.QFileDialog.getExistingDirectory(self,"Select Directory for save Files 2 : ",self.pathSave2))
        self.config.setValue("Dossier2"+"/pathSave",self.pathSave2)
        self.labelPathSave2.setText(self.pathSave2)
    
    def actionBrowse3(self):
        
        self.path3=self.config.value("Dossier3"+"/path")
        self.path3=str(QtGui.QFileDialog.getExistingDirectory(self,"Select Directory for Path 3 : ",self.path3))
        self.config.setValue("Dossier3"+"/path",self.path3)
        self.labelPath3.setText(self.path3)
         
    def actionBrowseSave3(self):
        
        self.pathSave3=self.config.value("Dossier"+"/pathSave")
        self.pathSave3=str(QtGui.QFileDialog.getExistingDirectory(self,"Select Directory for save Files 3 : ",self.pathSave3))
        self.config.setValue("Dossier3"+"/pathSave",self.pathSave3)
        self.labelPathSave3.setText(self.pathSave3)
      
    def pathChange (self):
        
        self.path1=self.labelPath1.text()
        self.pathSave1=self.labelPathSave1.text()
        self.config.setValue("Dossier1"+"/pathSave",self.pathSave1)
        self.config.setValue("Dossier1"+"/path",self.path1)
     
        self.path2=self.labelPath2.text()
        self.pathSave2=self.labelPathSave2.text()
        self.config.setValue("Dossier2"+"/pathSave",self.pathSave2)
        self.config.setValue("Dossier2"+"/path",self.path2)
        
        self.path3=self.labelPath3.text()
        self.pathSave3=self.labelPathSave3.text()
        self.config.setValue("Dossier3"+"/pathSave",self.pathSave3)
        self.config.setValue("Dossier3"+"/path",self.path3)
     
        
class ThreadRunAuto(QtCore.QThread):
    ## thread pour lancer en continu la lecture des images 
    
    
    def __init__(self, parent=None):
        
        super(ThreadRunAuto,self).__init__(parent)
        self.stopRunAcq=False
        self.config = QtCore.QSettings('confSave.ini', QtCore.QSettings.IniFormat)
        self.nbShoot=0
        self.parent=parent
        self.sepa=os.sep
    
    def run(self):
        global data
        print('-----> Start .... ')
        
        while True :
            if self.stopRunAcq:
                print('-----> end...') # stop the thread
                break
                
            
            chemin1=self.parent.path1
            chemin1=os.path.normpath(chemin1)
            chemin2=self.parent.path2
            chemin2=os.path.normpath(chemin2)
            chemin3=self.parent.path3
            chemin3=os.path.normpath(chemin3)
            
            newest1 = max([os.path.join(chemin1,d) for d in os.listdir(chemin1)],key=os.path.getmtime)
            newest2 = max([os.path.join(chemin2,d) for d in os.listdir(chemin2)],key=os.path.getmtime)
            newest3 = max([os.path.join(chemin3,d) for d in os.listdir(chemin3)],key=os.path.getmtime)
            
            
            #os.path.getmtime return time of last modicification of path 
            # max(glob.iglob(chemin+ '/'+'*.*'), key=os.path.getmtime) # comparaison fichier nouveau et ancien
            
            filename1= str(self.config.value("Dossier1"+"/lastFichier"   )) 
            filename2= str(self.config.value("Dossier2"+"/lastFichier"   )) 
            filename3= str(self.config.value("Dossier3"+"/lastFichier"   )) 
            time.sleep(0.1)
            
            if filename1==[] or newest1==[]:
                pass # print "fichier nul",filename
            if filename1==newest1 : # l ancien fichier est le meme que le nouveau
                pass # print "on fait rien.."
            if filename1!=newest1 or filename2!=newest2 or filename3!=newest3: 
                # un fichier different 
                print("un nouveau fichier est apparru")
                start=time.time() # on demare le chrono
                tps=0
                self.nbShoot=self.nbShoot+1  
                while tps<self.parent.waitValue:  #pendant le chrono on sauvegarde les fichiers nouveau avec comme extension le numero du shoot
                    if filename1!=newest1:
                        filename1=newest1   
                        self.config.setValue("Dossier1"+"/lastFichier",filename1)
                        self.config.sync()
                        
                        file1, fileExtension1 = os.path.splitext(filename1)
                        print(file1)
                        file1=basename(file1)
                        print(file1)
                        shutil.copyfile(newest1, self.parent.pathSave1+self.sepa+file1+'_'+str(self.nbShoot)+fileExtension1)#Path(newest1.stem))
                        print("copy file1",newest1,'to',self.parent.pathSave1+self.sepa+file1+'_'+str(self.nbShoot)+fileExtension1)
                    if filename2!=newest2:
                        filename2=newest2   
                        self.config.setValue("Dossier2"+"/lastFichier",filename2)
                        print("copy file2",newest2)
                        
                        file2, fileExtension2 = os.path.splitext(filename2)
                        file2=basename(file2)
                        
                        print("copy to",self.parent.pathSave2+self.sepa+file2+'_'+str(self.nbShoot)+fileExtension2)
                        shutil.copyfile(newest2, self.parent.pathSave2+file2+'_'+str(self.nbShoot)+fileExtension2)#Path(newest1.stem))
                    if filename3!=newest3:
                        filename3=newest3   
                        self.config.setValue("Dossier3"+"/lastFichier",filename3)
                        print("copy file3",newest3)
                        file3, fileExtension3 = os.path.splitext(filename3)
                        file3=basename(file3)
                        shutil.copyfile(newest3, self.parent.pathSave3+self.sepa+file3+'_'+str(self.nbShoot)+fileExtension3)#Path(newest1.stem))
                    time.sleep(0.1)
                    #print('on regarde pendant", xs si un autre fichier apparait et on le save avec le meme numero')
                    end=time.time()
                    tps=end-start
                    print("tps",tps)
                self.config.sync()
                
                
                
             
                    
    def stopThreadRunAuto(self):
        self.stopRunAcq=True
        
if __name__ == "__main__":
    appli = QtGui.QApplication(sys.argv)    
    l = MAINSAVE()#ThreadRunAuto()   
    l.show()
    # l.start()
    appli.exec_()