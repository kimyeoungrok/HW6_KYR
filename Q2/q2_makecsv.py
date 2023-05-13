#!/usr/bin/env python
# coding: utf-8

# In[13]:


import csv
import random

f = open('q2.csv','w',newline='')
wr = csv.writer(f)
dice = []
dice.append('100회')
for i in range(100):
    ran = random.randint(1,6)
    dice.append(ran)
wr.writerow(dice)

dice = []
dice.append('1,000회')
for i in range(1000):
    ran = random.randint(1,6)
    dice.append(ran)

wr.writerow(dice)
dice = []
dice.append('10,000회')
for i in range(10000):
    ran = random.randint(1,6)
    dice.append(ran)

wr.writerow(dice)
dice = []
dice.append('100,000회')
for i in range(100000):
    ran = random.randint(1,6)
    dice.append(ran)

wr.writerow(dice)

f.close()


# In[ ]:





# In[ ]:




