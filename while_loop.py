# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 14:59:36 2019

@author: Sakshi
"""

i = 1
while i<=5:
    print("h")
    i=i+1
######second program    
j = 1
while(j<=100):
    if(j%3 == 0 or j%5 == 0):
       print(end="") 
    else:
       print(j)
    j=j+1
#####third program
s = 1
while s<5:
    k=1
    while k<5:
        print("#",end="")
        k = k+1
    s=s+1
    print(" ")
    
###perfect square number
i = 1
while i<=500:
    j=1    
    while j*j<=i:
        if(j*j==i):
            print (i)
        j=j+1
    i=i+1
        
    
    