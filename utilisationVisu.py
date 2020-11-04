#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 16:29:24 2020

@author: juliengautier
"""
#pip install pyqtgraph
#pip install visu

#graph1: plot 2D
#graph2: plot 1D


from visu.WinCut import GRAPHCUT 
from visu import SEE
import sys
from PyQt5.QtWidgets import QApplication
import qdarkstyle
appli = QApplication(sys.argv) 
appli.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5()) 
a=[2,3,7,-5]
b=[-2,4,5,7]

graph1=SEE()
graph2=GRAPHCUT(meas=False,symbol=False)

graph2.PLOT(a,b) #a =f(b)
#graph1.PLOT(a) a fontion  du numerop de pixel 

graph1.show()
graph2.show()
appli.exec_() 

