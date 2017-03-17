# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 18:34:26 2017

@author: Sameer and Dad
"""

import pandas as pd
import matplotlib.pyplot as plt

habit = pd.read_csv('h_w.csv')
yes = habit[habit['habit_watching']=='Yes']
no = habit[habit['habit_watching']=='No']
print(yes)
print(no)

s = []
for i in yes['Age']:
    s.append(i)
print(s)
print(len(s))

s1 =[]
for i in no['Age']:
    s1.append(i)
print(s1)
print(len(s1))

labels = 'Yes','No'
sizes = [len(s),len(s1)]
explode = (0,0)
fig,ax1 = plt.subplots()
ax1.pie(sizes,labels=labels,explode=explode,shadow=True,startangle=90,autopct='%1.1f%%')
ax1.axis('equal')
plt.title('watching habits of the people for their subscribed channels')
plt.show()

print('\t Here is the watching habits of the people for their subscribed channel')    
    