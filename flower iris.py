# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 16:21:17 2017

@author: Sameer and Dad
"""

import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
iris = pd.read_csv("IRIS.csv")
seto = iris[iris['class']=='setosa']
versi = iris[iris['class']=='versicolor']
virgin = iris[iris['class']=='virginica']
print(seto)
print(versi)
print(virgin)

def setoo(data):
    seta = []
    for i in data['petal len']:
        seta.append(i)
    seta = sorted(seta)
    return seta

def versii(data):
    color = []
    for i in data['petal wid']:
        color.append(i)
    color = sorted(color)
    return color

def virginii(data):
    nica = []
    for i in data['sepal len']:
        nica.append(i)
    nica = sorted(nica)
    return nica

def svv(data):
    sevevi = []
    for i in data['sepal wid']:
        sevevi.append(i)
    sevevi = sorted(sevevi)
    return sevevi
    
def mean(data):
    return (sum(data)/len(data))
    
def var(data):
    flo = []
    for i in data:
        flo.append(math.pow((i-mean(data)),2))
    flo = sorted(flo)
    return(sum(flo)/len(flo))

def stdv(data):
    return math.sqrt(var(data))

def dstats(data):
    petall = []
    for i in data['petal len']:
        petall.append(i)
    petalw = []
    for i in data['petal wid']:
        petalw.append(i)
    sepall = []
    for i in data['sepal len']:
        sepall.append(i)
    sepalw = []
    for i in data['sepal wid']:
        sepalw.append(i)
    
    print("\t Mean of petal-len",mean(petall))
    print("\t Mean of petal-wid",mean(petalw))
    print("\t Mean of sepal-len",mean(sepall))
    print("\t Mean of sepal-wid",mean(sepalw))
    print("\t standard of deviation petal-len",stdv(petall))
    print("\t standard of deviation petal-wid",stdv(petalw))
    print("\t standard of deviation sepal-len",stdv(sepall))
    print("\t standard of deviation sepal-wid",stdv(sepalw))
    print("\t kurtosis of petal-len",scipy.stats.kurtosis(petall))
    print("\t kurtosis of petal-wid",scipy.stats.kurtosis(petalw))
    print("\t kurtosis of sepal-len",scipy.stats.kurtosis(sepall))
    print("\t kurtosis of sepal-wid",scipy.stats.kurtosis(sepalw))
print("\n SETOSA")
dstats(seto)
print("\n VERSICOLOR")
dstats(versi)
print("\n VIRGINICA")
dstats(virgin)

s1 = setoo(seto)
s2 = np.arange(len(s1))
s3 = setoo(versi)
s4 = np.arange(len(s3))
s5 = setoo(virgin)
s6 = np.arange(len(s5))

s7 = versii(seto)
s8 = np.arange(len(s7))
s9 = versii(versi)
s10 = np.arange(len(s9))
s11 = versii(virgin)
s12 = np.arange(len(s11))

s13 = virginii(seto)
s14 = np.arange(len(s13))
s15 = virginii(versi)
s16 = np.arange(len(s15))
s17 = virginii(virgin)
s18 = np.arange(len(s17))

s19 = svv(seto)
s20 = np.arange(len(s19))
s21 = svv(versi)
s22 = np.arange(len(s21))
s23 = svv(virgin)
s24 = np.arange(len(s23))

plt.plot(s2,s1,"r",s8,s7,"k",s14,s13,"b",s20,s19,"c",label = "setosa")
plt.plot(s4,s3,"r",s10,s9,"k",s16,s15,"b",s22,s21,"c",label = "versicolor")
plt.plot(s6,s5,"r",s12,s11,"k",s18,s17,"b",s24,s23,"c",label = "virginica")
plt.title("Flower IRIS")
plt.grid(True)
#plt.legend(loc = "upper left")
plt.show()

"""
I couldn't give legends because ... It's taking the whole area of the graph box... 
proper graph is not seen .....so...
And even colors are limited....
"""
