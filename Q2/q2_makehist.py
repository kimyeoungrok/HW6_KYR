#!/usr/bin/env python
# coding: utf-8

# In[24]:


import csv
import matplotlib.pyplot as plt

f=open('q2.csv','r')
data = csv.reader(f)


plt.rc('font',family="Malgun Gothic")
plt.rcParams['axes.unicode_minus']=False
number = [1,2,3,4,5,6]
for row in data:
    dice = []
    count=[0,0,0,0,0,0]
    for i in range(1,len(row)):
        dice.append(row[i])
        count[int(row[i])-1] += 1
    dice.sort()
    
    plt.title(row[0] + "주사위를 던졌을때")
    plt.hist(dice, bins=6, color='r')
    for i in range(len(count)):
        height = count[i]
        plt.text(number[i]-1, height, '%d' %height, ha='center', va='bottom', size = 12)
    plt.xlabel('나온 숫자')
    plt.ylabel('횟수')
    plt.show()
    
f.close()


# In[ ]:





# In[ ]:




