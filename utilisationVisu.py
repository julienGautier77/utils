
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
from visu.visual2 import SEE2
from visu.visualLight2 import SEELIGHT
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QVBoxLayout

import qdarkstyle
# from PyQt5.QtWidgets import QMainWindows
appli = QApplication(sys.argv) 

a=[2,3,7,-5]
b=[-2,4,5,7]

confpathVisu='/Users/juliengautier/Dropbox (LOA)/Programmes Python/princeton/confVisu.ini'

graph1=SEE2(confpath=confpathVisu,name='camA',roiCross=True)
# graph2=SEELIGHT(confpath=confpathVisu,name='camA')
# graph3=SEELIGHT(confpath=confpathVisu,name='camA')
# graph4=SEELIGHT(confpath=confpathVisu,name='camA')
# graph5=SEE2(confpath=confpathVisu,name='camA')
# graph6=SEE2(confpath=confpathVisu,name='camA')

# aa=QWidget()

# hLayout1=QHBoxLayout()
# hLayout1.addWidget(graph1)
# hLayout1.addWidget(graph2)
# hLayout1.addWidget(graph3)
# hLayout2=QHBoxLayout()
# hLayout2.addWidget(graph4)
# hLayout2.addWidget(graph5)
# hLayout2.addWidget(graph6)

# vLayout=QVBoxLayout()
# vLayout.addLayout(hLayout1)
# vLayout.addLayout(hLayout2)

# #graph2=GRAPHCUT(meas=False,symbol=False)

# #graph2.PLOT(a,b) #a =f(b)
# #graph1.PLOT(a) a fontion  du numerop de pixel 
# aa.setLayout(vLayout)

# aa.show()
graph1.show()
appli.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5()) 
appli.exec_() 

