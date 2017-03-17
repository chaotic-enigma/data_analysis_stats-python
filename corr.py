# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 22:04:01 2017

@author: Saif
"""

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

def corre(dx,dy):
    x = np.array(dx)
    y = np.array(dy)
    u = len(dx)*sum(x*y)-(sum(dx)*sum(dy))
    v = math.sqrt((len(dx)*sum(x**2)-(sum(x))**2)*(len(dx)*sum(y**2)-(sum(y))**2))
    r = u/v
    return(r)

corelation = pd.read_csv("corr.csv")

total = corelation['earning?']
#print(total)
lis = list(corelation['earning?'])
print(lis)
total1 = corelation[' channel ']
#print(total1)
lis1 = list(corelation[' channel '])
print(lis1)
print(corre(lis,lis1))
plt.scatter(lis,lis1)
plt.show()

total2 = corelation['why']
#print(total2)
lis2 = list(corelation['why'])
print(lis2)
total3 = corelation['pref']
#print(total3)
lis3 = list(corelation['pref'])
print(lis3)
print(corre(lis2,lis3))
plt.scatter(lis2,lis3)
plt.show()

total4 = corelation['Subscriptions']
#print(total4)
lis4 = list(corelation['Subscriptions'])
print(lis4)
total5 = corelation['h_w']
#print(total5)
lis5 = list(corelation['h_w'])
print(lis5)
print(corre(lis4,lis5))
plt.scatter(lis4,lis5)
plt.show()
