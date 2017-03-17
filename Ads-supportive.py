# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 18:22:03 2017

@author: Sameer and Dad
"""

import pandas as pd
import matplotlib.pyplot as plt

ads = pd.read_csv('adv.csv')
no = ads[ads['Ads?']=='No, I get vexed.']
yes = ads[ads['Ads?']=='Yes, which are relevant to me.']
print(no)
print(yes)

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

labels = 'no','yes'
sizes = [len(s),len(s1)]
explode = (0,0)
fig1,ax1 = plt.subplots()
ax1.pie(sizes,labels=labels,explode=explode,shadow=True,startangle=90,autopct='%1.1f%%')
plt.title('Details about whether they are supportive to Ads')
ax1.axis('equal')
plt.show()

print("\t Here is the analysis of the people's opinion for the Ads")