# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 18:29:36 2017

@author: Sameer and Dad
"""

import pandas as pd
import matplotlib.pyplot as plt

time = pd.read_csv("Time_spent.csv")
less = time[time['Time Spent']=='Less than 1 hour']
one = time[time['Time Spent']=='1 - 2 hours']
two = time[time['Time Spent']=='2 - 4 hours']
four = time[time['Time Spent']=='4 or more']
print(less)
print(one)
print(two)
print(four)

a = []
for i in less['Age']:
    a.append(i)
print(a)
print(len(a))

s = []
for i in one['Age']:
    s.append(i)
print(s)
print(len(s))

s1 = []
for i in two['Age']:
    s1.append(i)
print(s1)
print(len(s1))

s2 = []
for i in four['Age']:
    s2.append(i)
print(s2)
print(len(s2))

labels = 'Less than 1 hour','1 - 2 hours','2 - 4 hours','4 or more'
sizes = [len(a),len(s),len(s1),len(s2)]
explode = (0,0,0,0)
fig1,ax1 = plt.subplots()
ax1.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=200)
ax1.axis('equal')
plt.title('Time_spent')
plt.show()

print("\t Here is the habit of the people on watching videos on the basis spending time daily...")

