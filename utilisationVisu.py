
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 16:29:24 2020

@author: juliengautier
"""

import os
from visu.WinCut import GRAPHCUT 
from visu.visual import SEE

import sys
from PyQt6.QtWidgets import QApplication
import qdarkstyle

appli = QApplication(sys.argv) 
graph1=SEE()
graph1.show()
appli.exec_() 

