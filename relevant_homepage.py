# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 20:21:04 2017

@author: Sameer and Dad
"""

import pandas as pd
import matplotlib.pyplot as plt

relevant = pd.read_csv('relevant_homepage.csv')
one = relevant[relevant['homepage']==1]
two = relevant[relevant['homepage']==2]
three = relevant[relevant['homepage']==3]
four = relevant[relevant['homepage']==4]
five = relevant[relevant['homepage']==5]
print(one)
print(two)
print(three)
print(four)
print(five)

s = []
for i in one['Age']:
    s.append(i)
print(s)
print(len(s))

s1 = []
for i in two['Age']:
    s1.append(s1)
print(s1)
print(len(s1))

s2 = []
for i in three['Age']:
    s2.append(i)
print(s2)
print(len(s2))

s3 = []
for i in four['Age']:
    s3.append(i)
print(s3)
print(len(s3))

s4 = []
for i in five['Age']:
    s4.append(i)
print(s4)
print(len(s4))

labels = 'One','Two','Three','Four','Five'
sizes = [len(s),len(s1),len(s2),len(s3),len(s4)]
explode = (0,0,0,0,0)
fig1,ax1 = plt.subplots()
ax1.pie(sizes,labels=labels,explode=explode,shadow=True,startangle=220,autopct='%1.1f%%')
ax1.axis('equal')
plt.title('Feeling to the videos on their home-page')
plt.show()

print('\t Here is the analysis of the people showing their feeling to the videos on their homepage whether those sre for then or not\n 1-Junk, 5-Best and rest comes in between')


