# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 20:30:36 2017

@author: Sameer and Dad
"""

import pandas as pd
import matplotlib.pyplot as plt

circulate = pd.read_csv("vanish.csv")
yes = circulate[circulate['history']=='Yes']
no = circulate[circulate['history']=='No']
sometimes = circulate[circulate['history']=='Sometimes I do ...']
print(yes)
print(no)
print(sometimes)

s = []
for i in yes['Age']:
    s.append(i)
print(s)
print(len(s))

s1 = []
for i in no['Age']:
    s1.append(i)
print(s1)
print(len(s1))

s2 = []
for i in sometimes['Age']:
    s2.append(i)
print(s2)
print(len(s2))

labels = 'Yes','No','Sometimes I do'
sizes = [len(s),len(s1),len(s2)]
explode = (0,0,0)
fig1,ax1 = plt.subplots()
ax1.pie(sizes,labels=labels,explode=explode,startangle=100,autopct='%1.1f%%',shadow=True)
ax1.axis('equal')
plt.title('vanish-history')
plt.show()

print('\t Here is the analysis of the people who vanish history after watching the video on YouTube')

