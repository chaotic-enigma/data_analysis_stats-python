# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 21:00:53 2017

@author: Saif
"""

import pandas as pd
import matplotlib.pyplot as plt

forward = pd.read_csv('sharing.csv')
no = forward[forward['circulate']=='No']
yes = forward[forward['circulate']=='Yes']
sometimes = forward[forward['circulate']=='Sometimes']
print(no)
print(yes)
print(sometimes)

s = []
for i in no['Age']:
    s.append(i)
print(s)
print(len(s))

s1 = []
for i in yes['Age']:
    s1.append(i)
print(s1)
print(len(s1))

s2 = []
for i in sometimes['Age']:
    s2.append(i)
print(s2)
print(len(s2))

labels = 'no','yes','sometimes'
sizes = [len(s),len(s1),len(s2)]
explode = (0,0,0)
fig1,ax1 = plt.subplots()
ax1.pie(sizes,labels=labels,explode=explode,shadow=True,startangle=90,autopct='%1.1f%%')
plt.title('Details about their circulation on other social medias')
ax1.axis('equal')
plt.show()

print('\t Here is the analysis of the people on their sharing basis...')