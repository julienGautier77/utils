#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:41:47 2020

@author: juliengautier
"""

from PyQt5.QtWidgets import QApplication,QVBoxLayout,QHBoxLayout,QWidget,QPushButton,QGridLayout
from PyQt5.QtWidgets import QInputDialog,QSlider,QCheckBox,QLabel,QSizePolicy,QMenu,QMessageBox,QSpinBox
from PyQt5.QtWidgets import QShortcut
from pyqtgraph.Qt import QtCore,QtGui 
from PyQt5.QtCore import Qt
import sys

class WIND(QWidget):
    def __init__(self): # on peut mettre de variable apres (self,var1,...)
        # effectue une seule fois quand on demare la class
        super(WIND, self).__init__() # permet d'initialiser la class WIND avec init de la la class Qwidget dont elle depend
        self.setup()
        self.ActionButton()
    
    def setup(self):
        
        self.vbox1=QVBoxLayout() #layout Vertical boite qui permet de gerer mieux l affichage
        self.hbox2=QHBoxLayout()
        
        self.Button1=QPushButton('Bouton 1',self)
        self.Button2=QPushButton('Bouton 2',self)
        
        self.hbox2.addWidget(self.Button1)
        self.hbox2.addWidget(self.Button2)
        
        self.vbox1.addLayout(self.hbox2)
        
        self.Button3=QPushButton('Bouton 3',self)
        self.vbox1.addWidget(self.Button3)
        
        self.grid_layout = QGridLayout() # permet d'afficher suivant une grille 
        self.checkBox1=QCheckBox('Check box',self)
        self.labelBox2=QLabel('LAbel :',self)
        self.box3=QSpinBox(self)
        self.grid_layout.addWidget(self.checkBox1, 0, 0)
        self.grid_layout.addWidget(self.labelBox2,1,0)
        self.grid_layout.addWidget(self.box3, 0, 1)
    
        self.vbox1.addLayout(self.grid_layout)
        
        hMainLayout=QHBoxLayout()
        hMainLayout.addLayout(self.vbox1)
        
        self.setLayout(hMainLayout)  # 
    
    def ActionButton(self): # definition de ce qui se passe quand tu clique
        self.box3.editingFinished.connect(self.Actionbox)
        self.Button1.clicked.connect(self.ActionButton1)
        self.checkBox1.stateChanged.connect(self.ActionCheckBox1)
        
    def Actionbox(self):
        print('box', self.box3.value())
    
    def ActionButton1(self):
        print('action button1')
        
    def ActionCheckBox1(self):
        print('action')
        
if __name__ == "__main__":
    
    appli = QApplication(sys.argv) 
    #appli.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5()) Si tu veux en noir 
    e = WIND()
    e.show()
    appli.exec_()     
        
        