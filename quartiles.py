# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 16:29:36 2017

@author: Sameer and Dad
"""

def quartile(data):
    s = len(data)
    a = 1
    i = []
    while(a<4):
        q = a*(s+1)/4
        a = a+1
        i.append(q)
    return i
print(quartile([1,2,3,4,5,6,7,8,9,10]))
    

def decile(data):
    s1 = len(data)
    a1 = 1
    i1 = []
    while(a1<10):
        q1 = a1*(s1+1)/10
        a1 = a1+1
        i1.append(q1)
    return i1
print(decile([1,2,3,4,5,6,7,8,9,10]))


def percentile(data):
    s2 = len(data)
    a2 = 1
    i2 = []
    while(a2<100):
        q2 = a2*(s2+1)/100
        a2 = a2+1
        i2.append(q2)
    return i2
print(percentile([1,2,3,4,5,6,7,8,9,10]))
    