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
import pyqtgraph as pg 
import sys
import numpy  as np


class WIND(QWidget):
    def __init__(self): # 
        # done  when you start the class 
        super(WIND, self).__init__() # permet d'initialiser la class WIND avec init de la la class Qwidget dont elle depend
        self.setup()
        self.ActionButton()
    
    def setup(self):
        
        self.vbox1=QVBoxLayout() #layout Vertical box 
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
        
        
        ### add a  2D pyqrgraph 
        
        
        self.winImage = pg.GraphicsLayoutWidget()
        
        self.winImage.setAspectLocked(True)
        self.winImage.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        
        self.vbox2=QVBoxLayout()
       
        self.vbox2.addWidget(self.winImage)
        self.vbox2.setContentsMargins(0,0,0,0)
        
        self.p1=self.winImage.addPlot()
        self.imh=pg.ImageItem()
        self.axeX=self.p1.getAxis('bottom')
        self.axeY=self.p1.getAxis('left')
        self.p1.addItem(self.imh)
        self.p1.setMouseEnabled(x=False,y=False)
        self.p1.setContentsMargins(0,0,0,0)
   
        self.p1.setAspectLocked(True,ratio=1)
        self.p1.showAxis('right',show=False)
        self.p1.showAxis('top',show=False)
        self.p1.showAxis('left',show=True)
        self.p1.showAxis('bottom',show=True)
        
        self.data=np.random.rand(350, 400)
        self.imh.setImage(self.data)
        
        hMainLayout.addLayout(self.vbox2)
        
        
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
        
        