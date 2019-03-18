# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 17:37:21 2018

@author: Sakshi
"""
import xlwt
import os
from datetime import datetime 
currentpath = os.getcwd()
print (currentpath)
path1 = "C:/Users/Sakshi/Desktop/python"
style1 = xlwt.easyxf('font : name Time New Roman, color-index red, bold on','#,##0.00')
style2 = xlwt.easyxf('font : name Rockwell, color-index blue,bold on','DD-MM-YY')                     
style3 = xlwt.easyxf('font : name Arial, color-index blue,bold on')
wb = xlwt.Workbook()
ws = wb.add_sheet('first sheet#f5')
ws.write(0,0,1234.567,style1)                  
ws.write(1,0,datetime.now(),style2)                  
ws.write(2,0,'first excel via python',style2)                  
ws.write(3,0,1)
ws.write(3,1,11)
ws.write(3,2,111)
ws.write(3,3,xlwt.Formula("A4+B4+C4"))
os.chdir(path1)
wb.save('alv.xls')
os.chdir(currentpath)