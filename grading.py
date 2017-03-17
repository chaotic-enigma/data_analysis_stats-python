# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 20:54:57 2017

@author: Sameer and Dad
"""

import pandas as pd
import matplotlib.pyplot as plt

grade = pd.read_csv('grade_media.csv')
one = grade[grade['Grading?']==1]
two = grade[grade['Grading?']==2]
three = grade[grade['Grading?']==3]
four = grade[grade['Grading?']==4]
five = grade[grade['Grading?']==5]
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
    s1.append(i)
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

labels = '1','2','3','4','5'
sizes = [len(s),len(s1),len(s2),len(s3),len(s4)]
explode = (0,0,0,0,0)
fig1,ax1 = plt.subplots()
ax1.pie(sizes,labels=labels,explode=explode,startangle=150,autopct='%1.1f%%',shadow=True)
ax1.axis('equal')
plt.title('Grading-analysis')
plt.show()

print('\t Here is the analysis of the people which they have graded to the media \n 1-Time_pass, 5-Best_media and the rest comes in between')

