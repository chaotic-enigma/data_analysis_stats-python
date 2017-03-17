# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 21:37:46 2017

@author: Sameer and Dad
"""

import pandas as pd
import matplotlib.pyplot as plt

technical = pd.read_csv('t_f_care.csv')

one = technical[technical['values']==1]
two = technical[technical['values']==2]
three = technical[technical['values']==3]
four = technical[technical['values']==4]
five = technical[technical['values']==5]
six = technical[technical['values']==6]
seven = technical[technical['values']==7]
eight = technical[technical['values']==8]
nine = technical[technical['values']==9]
ten = technical[technical['values']==10]
ele = technical[technical['values']==11]
twe = technical[technical['values']==12]
thir = technical[technical['values']==13]
print(one)
print(two)
print(three)
print(four)
print(five)
print(six)
print(seven)
print(eight)
print(nine)
print(ten)
print(ele)
print(twe)
print(thir)

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
    s3.append(i)
print(s3)
print(len(s3))

s5 = []
for i in six['Age']:
    s5.append(i)
print(s5)
print(len(s5))

s6 = []
for i in seven['Age']:
    s6.append(i)
print(s6)
print(len(s6))

s7 = []
for i in eight['Age']:
    s7.append(i)
print(s7)
print(len(s7))

s8 = []
for i in nine['Age']:
    s8.append(i)
print(s8)
print(len(s8))

s9 = []
for i in ten['Age']:
    s9.append(i)
print(s9)
print(len(s9))

s10 = []
for i in ele['Age']:
    s10.append(i)
print(s10)
print(len(s10))

s11 = []
for i in twe['Age']:
    s11.append(i)
print(s11)
print(len(s11))

s12 = []
for i in thir['Age']:
    s12.append(i)
print(s12)
print(len(s12))

labels = '1','2','3','4','5','6','7','8','9','10','11','12','13'
sizes = [len(s),len(s1),len(s2),len(s3),len(s4),len(s5),len(s6),len(s7),len(s8),len(s9),len(s10),len(s11),len(s12)]
explode = (0,0,0,0,0,0,0,0,0,0,0,0,0)
fig1,ax1 = plt.subplots()
ax1.pie(sizes,labels=labels,explode=explode,startangle=190,shadow=True)
ax1.axis('equal')
plt.title('Technical Features which they care much')
plt.show()

print('\t Here is the analysis of the people on which technical features they care much!\n Na-No ads, Nb-No buffering, U-User ratings and testimonials')

"""
    Here 1 to 13 numbers stands for different qualities... only the value has been taken into consideration.
"""
