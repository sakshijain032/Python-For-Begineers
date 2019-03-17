# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 18:30:18 2019

@author: Sakshi
"""
print("According to position")
def person(name,age):
    print("name =",name)
    print("age =",age-1)
    
person('sakshi',5)
print(" ")
print("According to keyword")
def person(name,age):
    print("name =",name)
    print("age =",age-1)
    
person(age = 5,name = 'sakshi')

print(" ")
print("According to default")
def person(name,age=18):
    print("name =",name)
    print("age =",age)
person("through default value") 
print(" ")
person('sakshi')#here if age is not given then it will take 18 as default & if you pass any
#value then it will override it
print(" ")
print("through override")
person('sakshi',19)
print(" ")
print ("Variable length argument")
def sum(*b):# b is tuple that is it can take any number of argument
    c = 0
    for i in b:
        c = c+i
    print("Sum =",c)
    
sum(1,2,3,4)
sum(2,3,4,5,5)
