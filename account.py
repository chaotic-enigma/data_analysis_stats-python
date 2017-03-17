# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 14:21:50 2017

@author: Sameer and Dad
"""


import pandas as pd
import matplotlib.pyplot as plt

analysis  = pd.read_csv("ASD.csv")

acc = analysis[analysis['Account ']==1]
ount = analysis[analysis['Account ']==0]
print(acc)
print(ount)

s = []
for i in acc['Age']:
    s.append(i)
print(s)
print(len(s))

s1 = []
for i in ount['Age']:
    s1.append(i)
print(s1)
print(len(s1))
"""
print("\n People who have an account on YouTube \n")
print(acc.values)
print("\n People who don't have an account on YouTube \n")
print(ount.values)
"""
#print(acc['Account ']==1)
#print(count['Account ']==0)

labels = 'Yes','No'
sizes = [len(s),len(s1)]
explode = (0,0)
fig1,ax1 = plt.subplots()
ax1.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('own-account')
plt.show()

print("\n\t Here, 0 stands for the people who don't have an account \n and 1 stands for the people who have....")

