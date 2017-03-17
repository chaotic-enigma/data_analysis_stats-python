# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 21:12:25 2017

@author: Sameer and Dad
"""

import pandas as pd
import matplotlib.pyplot as plt

channel_own = pd.read_csv('own_channel.csv')
yes_inactive = channel_own[channel_own[' channel ']=='Yes, but it is not active']
no = channel_own[channel_own[' channel ']=='No.']
yes_active = channel_own[channel_own[' channel ']=='Yes, it is active']
plans = channel_own[channel_own[' channel ']=='I will make my channel.']
print(yes_inactive)
print(no)
print(yes_active)
print(plans)

s = []
for i in yes_inactive['Age']:
    s.append(i)
print(s)
print(len(s))

s1 = []
for i in no['Age']:
    s1.append(i)
print(s1)
print(len(s1))

s2 = []
for i in yes_active['Age']:
    s2.append(i)
print(s2)
print(len(s2))

s3 = []
for i in plans['Age']:
    s3.append(i)
print(s3)
print(len(s3))

labels = 'yes_inactive','no','yes_active','plans'
sizes = [len(s),len(s1),len(s2),len(s3)]
explode = (0,0,0,0)
fig1,ax1 = plt.subplots()
ax1.pie(sizes,labels=labels,explode=explode,shadow=True,startangle=160,autopct='%1.1f%%')
ax1.axis('equal')
plt.title('Details about their channel')
plt.show()

print('\t Here is the analysis showing the details about their channel')

