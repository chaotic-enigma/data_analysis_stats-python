# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 18:45:49 2017

@author: Sameer and Dad
"""

import pandas as pd
import matplotlib.pyplot as plt

pawork = pd.read_csv('p_a_work.csv')
none = pawork[pawork['after_work']=='None.']
work = pawork[pawork['after_work']=='Work']
tv = pawork[pawork['after_work']=='Television ']
yt = pawork[pawork['after_work']=='Youtube']
print(none)
print(work)
print(tv)
print(yt)

s = []
for i in none['Age']:
    s.append(i)
print(s)
print(len(s))

s1 = []
for i in work['Age']:
    s1.append(i)
print(s1)
print(len(s1))

s2 = []
for i in tv['Age']:
    s2.append(i)
print(s2)
print(len(s2))

s3 = []
for i in yt['Age']:
    s3.append(i)
print(s3)
print(len(s3))

labels = 'None','Work','TV','YT'
sizes = [len(s),len(s1),len(s2),len(s3)]
explode = (0,0,0,0)
fig1,ax1 = plt.subplots()
ax1.pie(sizes,labels=labels,explode=explode,shadow=True,startangle=90,autopct='%1.1f%%')
ax1.axis('equal')
plt.title('What people do after their job')
plt.show()

print('\t Here is the analysis of the people on what they do after their work')
