# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 08:51:11 2017

@author: Sameer and Dad
"""

import pandas as pd
import matplotlib.pyplot as plt

earn = pd.read_csv('engage_earn.csv')
no = earn[earn['earning?']=='No']
yes = earn[earn['earning?']=='Yes']
plan = earn[earn['earning?']=='I am thinking to earn ...']
print(no)
print(yes)
print(plan)

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
for i in plan['Age']:
    s2.append(i)
print(s2)
print(len(s2))

labels = 'no','yes','planning'
sizes = [len(s),len(s1),len(s2)]
explode = (0,0,0)
fig1,ax1 = plt.subplots()
ax1.pie(sizes,labels=labels,explode=explode,shadow=True,startangle=90,autopct='%1.1f%%')
ax1.axis('equal')
plt.title('earning habits')
plt.show()

print('\t Here is the earning habits of people through YouTube')

