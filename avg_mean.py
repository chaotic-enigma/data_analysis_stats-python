# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 16:23:21 2017

@author: Sameer and Dad
"""

def mean(avg):
    s = 0
    for i in avg:
        s = s+i
    s1 = s/(len(avg))
    return s1
print(mean([1,0.5,2,-1,42]))


def harmean(data_set_1):
    n=[]
    for i in data_set_1:
        n.append(1/i)
    s = sum(n)
    hm = len(data_set_1)/s
    return hm
print(harmean([1,0.5,2,-1,42]))

def geomean(data_set_1):
    p=1
    for i in data_set_1:
        p = p*i
    gm = p**(1/len(data_set_1))
    return gm
print(geomean([1,0.5,-2,-1,42]))