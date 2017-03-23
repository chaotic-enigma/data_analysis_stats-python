# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 17:35:52 2017

@author: Sameer and Dad
"""

import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

nonlang = open("sanskrit.txt",'r+',encoding="utf-8")
nonlang = nonlang.read()
sans = nonlang.lower()
def eng(krit):
    krit = krit.lower()
    skips = ['.',',',';','"',"'",'$','!','?','-','@','(',')',
    '|','#','^','*','&','~','`','\n','%','{','}','_','+','=','num','</mula>\uf076\uf076\uf076<page',
    '[',']']
    for ch in skips:
        krit = krit.replace(ch,"")
    cia = Counter(krit.split(" "))
    return cia

#print(eng(sans))


s = eng(sans)
q = list(s.keys())
#print(q)

w = eng(sans)
f = list(w.values())
q = np.arange(0,len(f))
f = sorted(f,reverse = True)
#print(value)

#from collections import Counter
aralang = open("arabic.txt",'r+',encoding="utf-8")
aralang = aralang.read()
arabbi = aralang.lower()
def arabic(quran):
    quran = quran.lower()
    skips = ['.',',',';','"',"'",'$','!','?','-','@','(',')',
    '|','#','^','*','&','~','`','\n','%','{','}','_','+','=','num','</mula>\uf076\uf076\uf076<page',
    '[',']','\u202b\u202a','518c\u202c','c\u202c']
    for ch in skips:
        quran = quran.replace(ch,"")
    urdu = Counter(quran.split(" "))
    return urdu    
#print(arabic(arabbi))

k = arabic(arabbi)
key = list(k.keys())
#print(key)

v = arabic(arabbi)
value = list(v.values())
key = np.arange(0,len(value))
value = sorted(value,reverse = True)
#print(value)

plt.plot(key,value,"ko-",label = "arabic")
plt.plot(q,f,"md-",label = "sanskrit")
plt.xlabel("words")
plt.ylabel("repetition")
plt.title("WORD FREQUENCY")
plt.axis([0,75,0,500])
plt.legend(loc = "upper right")

