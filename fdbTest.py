# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 18:01:56 2022

@author: GAUTIER
"""
import fdb
import time
from pyqtgraph.Qt import QtCore

# si pas en local dsn=10.0.5.X/ ??

con = fdb.connect(dsn='C:\PilMotDB\PILMOTCONFIG.FDB', user='sysdba', password='masterkey')
cur = con.cursor()
# TABLE_NAME ='TbParameterSTR'#' TbEquipment'#
# # SELECT = 'select ADDRESS,PKID=1 from %s' % TABLE_NAME

# cur.execute("select * from %s " % (TABLE_NAME))
# # cur.execute(SELECT)
# print(cur.fetchall())

# IDDAME =1016 'Val1stepMotor '  TbParameterREAL
# 1104, 'UnitMotor    ') TbParameterSTR
# 1201 à 1210 Nom des positions Absolues de référence TbParameterSTR
# 1211 à 1220 Valeur des positions Absolues de référence TbParameterREA
#1001 Coefficient Axe TbParameterINT

# # Print a header.where IDNAME=1211
# for fieldDesc in cur.description:
#     print( fieldDesc[fdb.DESCRIPTION_NAME].ljust(fieldDesc[fdb.DESCRIPTION_DISPLAY_SIZE]))
# # print() # Finish the header with a newline.
# for (NAME, PKID) in cur:
    
#     print ('%s = %s.' % (NAME, PKID))

# For each row, print the value of each field left-justified within
# the maximum possible width of that field.




# for row in cur:
#     for fieldIndex in fieldIndices:
#         # print(fieldIndex)
#         fieldValue = str(row[fieldIndex])
#         print(fieldValue)
#         fieldMaxWidth = cur.description[fieldIndex][fdb.DESCRIPTION_DISPLAY_SIZE]
#         time.sleep(1)
#         # print (fieldValue.ljust(fieldMaxWidth) ,)

# # #     # print # Finish the row with a newline.


## Liste nom moteur
# TABLE_NAME ='TbEquipment'
# SELECT = 'select * from %s  '% TABLE_NAME
# #PKID,IDMODULE,IDNAME,VALPARAM,NUMAXI,CATEGORY
# cur.execute(SELECT)
# fieldIndices = range(len(cur.description))
# print('field',fieldIndices,cur.description)
# print('-'*50)
# print(cur.fetchall())
# for row in cur:
#     print(str(row[3]1)

#liste equipement :
TABLE_NAME ='TbEquipment'
SELECT = 'select * from %s  '% TABLE_NAME
#PKID,IDMODULE,IDNAME,VALPARAM,NUMAXI,CATEGORY
cur.execute(SELECT)
equip=[]
typeEquip=[] # nombre d ESBIM *2 = nb  of motors connected
for row in cur:
    equip.append(row[1])
    typeEquip.append(row[2])
print(equip,typeEquip)
# #IDNAME=10 : nom du rack

#Liste nom Rack
TABLE_NAME ='TbParameterSTR'
SELECT = 'select * from %s where IDNAME=10  '% TABLE_NAME
nomRack=[]
cur.execute(SELECT)
for row in cur:
    nomRack.append(str(row[3]))
# print(nomRack)

## Liste nom moteur
TABLE_NAME ='TbParameterSTR'
SELECT = 'select * from %s where IDNAME=2  '% TABLE_NAME
nomMoteur=[]
cur.execute(SELECT)
for row in cur:
    nomMoteur.append(str(row[3]))
# print(nomMoteur)


# liste pas dans l unite 

TABLE_NAME ='TbParameterREAL'
SELECT = 'select * from %s where IDNAME=1106  '% TABLE_NAME
pasMoteur=[]
cur.execute(SELECT)
for row in cur:
    pasMoteur.append(str(row[3]))
# print(pasMoteur)

# liste  unite 

TABLE_NAME ='TbParameterSTR'
SELECT = 'select * from %s where IDNAME=1104  '% TABLE_NAME
uniteMoteur=[]
cur.execute(SELECT)
for row in cur:
    uniteMoteur.append(str(row[3]))
# print(uniteMoteur)





# liste   reference absolute 
refName=["ref1Name","ref2Name","ref3Name","ref4Name","ref5Name","ref6Name"]
TABLE_NAME ='TbParameterSTR'
for u in range(0,6): 
    value=1201+u
    SELECT = 'select * from %s where IDNAME=%s '% (TABLE_NAME,str(value))
    refName[u]=[]
    cur.execute(SELECT)
    
    # print (cur.fetchall())
    for row in cur:
        refName[u].append(str(row[3]))
        
# print(refName[0])
# liste value of referecne position
refPos=["ref1Pos","ref2Pos","ref3Pos","ref4Pos","ref5Pos","ref6Pos"]
TABLE_NAME ='TbParameterREAL'
for u in range(0,6): 
    value=1211+u
    SELECT = 'select * from %s where IDNAME=%s '% (TABLE_NAME,str(value))
    refPos[u]=[]
    cur.execute(SELECT)
   
    for row in cur:
        refPos[u].append(str(row[3]))



#1009 Butée logicielle PLUS TbParameterINT
#1010 Butée logicielle MOINS TbParameterINT

# liste value of rlogiciel butee +
ButPlus=[]
TABLE_NAME ='TbParameterINT'
SELECT = 'select * from %s where IDNAME=%s '% (TABLE_NAME,str(1009))
cur.execute(SELECT)
for row in cur:
    ButPlus.append(str(row[3]))



# liste value of rlogiciel butee +
ButMoins=[]
TABLE_NAME ='TbParameterINT'
SELECT = 'select * from %s where IDNAME=%s '% (TABLE_NAME,str(1010))
cur.execute(SELECT)
for row in cur:
    ButMoins.append(str(row[3]))



for j in range (0,len(nomMoteur)):
    # nomMoteur[j]=nomMoteur[j].lstrip()
    if nomMoteur[j]==' ':
        nomMoteur[j]='M'+str(j)
    # nomMoteur[j]=nomMoteur[j].replace(' ','_'+str(j))
    nomMoteur[j]=nomMoteur[j].replace(' ','_')
    uniteMoteur[j]=uniteMoteur[j].replace('Â','')
    if  pasMoteur[j]=='0.0':
        pasMoteur[j]='1'
# print(nomMoteur)
conf=QtCore.QSettings('confMoteur.ini', QtCore.QSettings.IniFormat)
u=0
for j in range (0,len(equip)):
    # print('j=',j)
    for i in range (0,typeEquip[j]*2):
        # print(i+u)
        conf.setValue(nomMoteur[i+u]+"/nom",nomMoteur[i+u])
        conf.setValue(nomMoteur[i+u]+"/nomRack",nomRack[j])
        conf.setValue(nomMoteur[i+u]+"/IPRack",equip[j])
        conf.setValue(nomMoteur[i+u]+"/numESim",j)
        conf.setValue(nomMoteur[i+u]+"/numMoteur",i+1)
        conf.setValue(nomMoteur[i+u]+"/stepmotor",1/float(pasMoteur[i+u]))
        conf.setValue(nomMoteur[i+u]+"/unit",uniteMoteur[i+u])
        conf.setValue(nomMoteur[i+u]+"/buteePos",ButPlus[i+u])
        conf.setValue(nomMoteur[i+u]+"/buteeneg",ButMoins[i+u])
        conf.setValue(nomMoteur[i+u]+"/moteurType","RSAI")
        conf.setValue(nomMoteur[i+u]+"/rang",i+u)
        for v in range(0,6):
            conf.setValue(nomMoteur[i+u]+"/ref"+str(v)+"Name",refName[v][i+u])
            conf.setValue(nomMoteur[i+u]+"/ref"+str(v)+"Pos",refPos[v][i+u])
        conf.sync()
    u=u+i+1
   
    
value=1201
TABLE_NAME ='TbParameterSTR'
SELECT = 'select* from %s where IDNAME=%s '% (TABLE_NAME,str(value))

cur.execute(SELECT)
print(cur.fetchall())
for fieldDesc in cur.description:
    print( fieldDesc[fdb.DESCRIPTION_NAME].ljust(fieldDesc[fdb.DESCRIPTION_DISPLAY_SIZE]))
# print(cur.fetchall())
 # cur.execute('update TbParameterSTR

value=1201
IDMODULE=2
NUMAXIS=1
TABLE_NAME ='TbParameterSTR'
SELECT = 'select VALPARAM from %s where IDNAME=%s and IDMODULE=%d and NUMAXIS=%d '% (TABLE_NAME,str(value),IDMODULE,NUMAXIS)

cur.execute(SELECT)
result=cur.fetchone()[0]
print(result)
# print(cur.fetchall())
# for row in cur :
#     print(row)
#     print(row[0])
valPara='testpara'
IDNAME='1201'
IDMODULE=2
NUMAXIS=1
TABLE_NAME ='TbParameterSTR'
update= 'update %s set VALPARAM=%s where IDNAME=%s and IDMODULE=%d and NUMAXIS=%d CURRENT OF cur'% (TABLE_NAME,valPara, IDNAME,IDMODULE,NUMAXIS)

curUpdate = con.cursor()
curUpdate.execute(update)

cur.execute(SELECT)
result=cur.fetchone()[0]
print(result)




    
    