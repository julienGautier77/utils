
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



import os


from visu.WinCut import GRAPHCUT 
from visu.visual import SEE
from visu.visualLight import SEELIGHT
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QVBoxLayout

import qdarkstyle
# from PyQt5.QtWidgets import QMainWindows
appli = QApplication(sys.argv) 

a=[2,3,7,-5]
b=[-2,4,5,7]



graph1=SEE2()

graph1.show()
appli.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5()) 
appli.exec_() 

