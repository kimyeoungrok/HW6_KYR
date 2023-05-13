#!/usr/bin/env python
# coding: utf-8

# In[25]:


import csv
import matplotlib.pyplot as plt

f = open('subway_202303.csv','r')
data =csv.reader(f)
header = next(data)
header = next(data)

get_on = {}
#승차
for row in data:
    if row[3] != '':
        if row[10] == '':
            row[10] = '0'
        if row[12] == '':
            row[12] = '0'
        total = int(row[10]) + int(row[12])
        try:
            get_on[row[3]]+=total
        except KeyError as k:
            get_on[row[3]] = total
        finally:
            pass

values = list(get_on.values())
values.sort(reverse=True)
values = values[:30]
print(values)

station = []
key = list(get_on.keys())
for s in values:
    for k in key:
        if get_on[k] == s:
            station.append(k)
            break
            
print(station)


plt.rc('font',family="Malgun Gothic")
plt.rcParams['axes.unicode_minus']=False
plt.figure(figsize=(60,10))
plt.rc('xtick', labelsize=7)
plt.title("지하철 승차 승객수 많은 역 상위 30개")
plt.bar(station,values)
plt.xticks(rotation=60)
plt.text(station[0], values[0], '%d명' %values[0], ha='center', va='bottom', size = 12)
plt.text(station[29], values[29], '%d명' %values[29], ha='center', va='bottom', size = 12)
plt.xlabel('역 이름')
plt.ylabel('승객 수(07시 ~ 09시)')
plt.show()

f.close()


f = open('subway_202303.csv','r')
data =csv.reader(f)
header = next(data)
header = next(data)

get_off = {}
#하차
for row in data:
    if row[3] != '':
        if row[11] == '':
            row[11] = '0'
        if row[13] == '':
            row[13] = '0'
        total = int(row[11]) + int(row[13])
        try:
            get_off[row[3]]+=total
        except KeyError as k:
            get_off[row[3]] = total
        finally:
            pass

values = list(get_off.values())
values.sort(reverse=True)
values = values[:30]
print(values)

station = []
key = list(get_off.keys())
for s in values:
    for k in key:
        if get_off[k] == s:
            station.append(k)
            break
            
print(station)


plt.rc('font',family="Malgun Gothic")
plt.rcParams['axes.unicode_minus']=False
plt.figure(figsize=(60,10))
plt.rc('xtick', labelsize=7)
plt.title("지하철 하차 승객수 많은 역 상위 30개")
plt.bar(station,values)
plt.xticks(rotation=60)
plt.text(station[0], values[0], '%d명' %values[0], ha='center', va='bottom', size = 12)
plt.text(station[29], values[29], '%d명' %values[29], ha='center', va='bottom', size = 12)
plt.xlabel('역 이름')
plt.ylabel('승객 수(07시 ~ 09시)')
plt.show()

f.close()


f = open('subway_202303.csv','r')
data =csv.reader(f)
header = next(data)
header = next(data)

get_onoff = {}
#승하차
for row in data:
    if row[3] != '':
        if row[10] == '':
            row[10] = '0'
        if row[11] == '':
            row[11] = '0'
        if row[12] == '':
            row[12] = '0'
        if row[13] == '':
            row[13] = '0'
        total = int(row[11]) + int(row[13]) + int(row[10]) + int(row[12])
        try:
            get_onoff[row[3]]+=total
        except KeyError as k:
            get_onoff[row[3]] = total
        finally:
            pass

values = list(get_onoff.values())
values.sort(reverse=True)
values = values[:30]
print(values)

station = []
key = list(get_onoff.keys())
for s in values:
    for k in key:
        if get_onoff[k] == s:
            station.append(k)
            break
            
print(station)


plt.rc('font',family="Malgun Gothic")
plt.rcParams['axes.unicode_minus']=False
plt.figure(figsize=(60,10))
plt.rc('xtick', labelsize=7)
plt.title("지하철 승하차 승객수 많은 역 상위 30개")
plt.bar(station,values)
plt.xticks(rotation=60)
plt.text(station[0], values[0], '%d명' %values[0], ha='center', va='bottom', size = 12)
plt.text(station[29], values[29], '%d명' %values[29], ha='center', va='bottom', size = 12)
plt.xlabel('역 이름')
plt.ylabel('승객 수(07시 ~ 09시)')
plt.show()

f.close()


# In[ ]:




