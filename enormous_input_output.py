# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 20:48:28 2019

@author: Sakshi
"""
a,c=0,0
n,k =map(int,input().split())
for i in range (n):
    t = int(input())
    if (t%k==0):
        a+=1
    if (t>0):
        c=1
if (c==1):
      print(a)
else: 
    print("Enter atleast one positive value")

        
