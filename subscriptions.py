# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 08:04:05 2017

@author: Sameer and Dad
"""
import pandas as pd
import matplotlib.pyplot as plt

subscribe = pd.read_csv('subscriptions.csv')
low = subscribe[subscribe['Subscriptions']==3]
medium = subscribe[subscribe['Subscriptions']==6]
eight = subscribe[subscribe['Subscriptions']==8]
more = subscribe[subscribe['Subscriptions']==12]
no = subscribe[subscribe['Subscriptions']==0]
print(low)
print(medium)
print(eight)
print(more)
print(no)

s = []
for i in low['Age']:
    s.append(i)
print(s)
print(len(s))

s1 = []
for i in medium['Age']:
    s1.append(i)
print(s1)
print(len(s1))

s2 = []
for i in eight['Age']:
    s2.append(i)
print(s2)
print(len(s2))

s3 = []
for i in more['Age']:
    s3.append(i)
print(s3)
print(len(s3))

s4 = []
for i in no['Age']:
    s4.append(i)
print(s4)
print(len(s4))

labels = '3','6','8','12','0'
sizes = [len(s),len(s1),len(s2),len(s3),len(s4)]
explode = (0,0,0,0,0)
fig1,ax1 = plt.subplots()
ax1.pie(sizes,labels=labels,explode=explode,shadow=True,autopct='%1.1f%%',startangle=90)
ax1.axis('equal')
plt.title('subscriptions')
plt.show()

print('\t Here is the subscription habits of the people for the channels')
