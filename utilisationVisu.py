#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 16:29:24 2020

@author: juliengautier
"""
#pip install pyqtgraph
#pip install visu

from visu.WinCut import GRAPHCUT 
import sys
from PyQt5.QtWidgets import QApplication

appli = QApplication(sys.argv) 

a=[2,3,7,5]
b=[2,4,5,7]

graph1=GRAPHCUT()
graph2=GRAPHCUT()

graph1.PLOT(a,b) #a =f(b)
#graph1.PLOT(a) a fontion  du numerop de pixel  
graph1.show()
appli.exec_() 

