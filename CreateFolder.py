#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 16:18:32 2020

@author: juliengautier
"""
import os
import time
import pathlib
import numpy as np

A=[0,3,5]
B=[6,7,8]


foldername=time.strftime("%Y_%m_%d")  # Save img in a new folder with the time as namefile
filename='SauvegardeMot'
date=time.strftime("%Y_%m_%d_%H_%M_%S")

p=pathlib.Path(__file__)

print(foldername)

sepa=os.sep
pathAutoSave=str(p.parent)+sepa
print(pathAutoSave)


groupsName=[]
self.groups=self.conf.childGroups()
    for groups in self.groups:
        self.groupsName.append(self.conf.value(groups+"/nameCDD"))


if not os.path.isdir(pathAutoSave+foldername):
    os.mkdir(pathAutoSave+foldername)

fichier=pathAutoSave+foldername+sepa+filename
print(fichier)
saveData=np.array([A,B])
saveData=saveData.T
np.savetxt(str(fichier)+'.txt',saveData)
