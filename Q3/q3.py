#!/usr/bin/env python
# coding: utf-8

# In[20]:


import csv
import matplotlib.pyplot as plt

f_2010 = open('jeju_population_2010.csv','r')
f_2014 = open('jeju_population_2014.csv','r')
f_2018 = open('jeju_population_2018.csv','r')
f_2022 = open('jeju_population_2022.csv','r')


data_2010 = csv.reader(f_2010)
data_2014 = csv.reader(f_2014)
data_2018 = csv.reader(f_2018)
data_2022 = csv.reader(f_2022)

label = ['남자비율','여자비율']
color = ['blue','red']
#2010년 제주 인구 데이터
count = 0
data = []
title = ''
for row in data_2010:
    if count > 1:
        break
    
    if row[0] == '행정구역':
        title = row[1].split('_')[0]
    else:
        man = int(row[3].replace(',',''))
        woman = int(row[4].replace(',',''))
        data.append(man)
        data.append(woman)
    count += 1
    
print(data)
plt.rc('font',family="Malgun Gothic")
plt.rcParams['axes.unicode_minus']=False
plt.title(title + " 제주도 남녀 비율")
plt.pie(data, labels = label, autopct='%.2f%%', colors = color, explode=(0,0))
plt.legend()
plt.show()



#2014년 제주 인구 데이터
count = 0
data = []
title = ''
for row in data_2014:
    if count > 1:
        break
    
    if row[0] == '행정구역':
        title = row[1].split('_')[0]
    else:
        man = int(row[3].replace(',',''))
        woman = int(row[4].replace(',',''))
        data.append(man)
        data.append(woman)
    count += 1
    
print(data)
plt.rc('font',family="Malgun Gothic")
plt.rcParams['axes.unicode_minus']=False
plt.title(title + " 제주도 남녀 비율")
plt.pie(data, labels = label, autopct='%.2f%%', colors = color, explode=(0,0))
plt.legend()
plt.show()


#2018년 제주 인구 데이터
count = 0
data = []
title = ''
for row in data_2018:
    if count > 1:
        break
    
    if row[0] == '행정구역':
        title = row[1].split('_')[0]
    else:
        man = int(row[3].replace(',',''))
        woman = int(row[4].replace(',',''))
        data.append(man)
        data.append(woman)
    count += 1
    
print(data)
plt.rc('font',family="Malgun Gothic")
plt.rcParams['axes.unicode_minus']=False
plt.title(title + " 제주도 남녀 비율")
plt.pie(data, labels = label, autopct='%.2f%%', colors = color, explode=(0,0))
plt.legend()
plt.show()


#2022년 제주 인구 데이터
count = 0
data = []
title = ''
for row in data_2022:
    if count > 1:
        break
    
    if row[0] == '행정구역':
        title = row[1].split('_')[0]
    else:
        man = int(row[3].replace(',',''))
        woman = int(row[4].replace(',',''))
        data.append(man)
        data.append(woman)
    count += 1
    
print(data)
plt.rc('font',family="Malgun Gothic")
plt.rcParams['axes.unicode_minus']=False
plt.title(title + " 제주도 남녀 비율")
plt.pie(data, labels = label, autopct='%.2f%%', colors = color, explode=(0,0))
plt.legend()
plt.show()
        
    
    
f_2010.close()
f_2014.close()
f_2018.close()
f_2022.close()


# In[ ]:





# In[ ]:




