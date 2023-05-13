#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
import matplotlib.pyplot as plt

korea_file = open('q1_korea.csv','r')
seoul_file = open('q1_seoul.csv','r')
deajeon_file = open('q1_daejeon.csv','r')
busan_file = open('q1_busan.csv','r')
jeju_file = open('q1_jeju.csv','r')

korea_data = csv.reader(korea_file)
seoul_data = csv.reader(seoul_file)
deajeon_data = csv.reader(deajeon_file)
busan_data = csv.reader(busan_file)
jeju_data = csv.reader(jeju_file)

header = next(korea_data)
header = next(seoul_data)
header = next(deajeon_data)
header = next(busan_data)
header = next(jeju_data)

korea = []
seoul = []
deajeon = []
busan = []
jeju = []

month = ['JAN','Feb','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']

for row in korea_data :
    if row[2] != '':
        korea.append(float(row[2]))
        
for row in seoul_data:
    if row[2] != '':
        seoul.append(float(row[2]))


for row in deajeon_data:
    if row[2] != '':
        deajeon.append(float(row[2]))
for row in busan_data:
    if row[2] != '':
        busan.append(float(row[2]))
for row in jeju_data:
    if row[2] != '':
        jeju.append(float(row[2]))
        
plt.rc('font',family="Malgun Gothic")
plt.rcParams['axes.unicode_minus']=False
plt.title("2022년 지역별 월평균 기온 추이")
plt.xlabel('월')
plt.ylabel('기온(℃)')
plt.plot(month,korea, color='red', label='전국') 
plt.plot(month,seoul, color='orange',label='서울')
plt.plot(month,deajeon, color='yellow', label='대전') 
plt.plot(month,busan, color='green',label='부산')
plt.plot(month,jeju, color='blue', label='제주') 
plt.legend()
plt.show()

diff = []
for i in range(0,12):
    diff.append(seoul[i]-korea[i])
plt.title("서울월평균 기온 - 전국 월평균 기온")
plt.xlabel('월')
plt.ylabel('기온차이(℃)')
plt.bar(month, diff)
for i in range(len(month)):
    height = diff[i]
    plt.text(month[i], 0, '%.1f' %height, ha='center', va='bottom', size = 12)
plt.show()


#plt.title("2022년 전국/대전 월평균 기온 추이")
#plt.xlabel('월')
#plt.ylabel('기온(℃)')
#plt.plot(month,korea, color='red', label='전국') 
#plt.plot(month,deajeon, color='orange',label='대전')
#plt.legend()
#plt.show()

diff = []
for i in range(0,12):
    diff.append(deajeon[i]-korea[i])
plt.title("대전월평균 기온 - 전국 월평균 기온")
plt.xlabel('월')
plt.ylabel('기온차이(℃)')
plt.bar(month, diff)
for i in range(len(month)):
    height = diff[i]
    plt.text(month[i], 0, '%.1f' %height, ha='center', va='bottom', size = 12)
plt.show()


#plt.title("2022년 전국/부산 월평균 기온 추이")
#plt.xlabel('월')
#plt.ylabel('기온(℃)')
#plt.plot(month,korea, color='red', label='전국') 
#plt.plot(month,busan, color='orange',label='부산')
#plt.legend()
#plt.show()

diff = []
for i in range(0,12):
    diff.append(busan[i]-korea[i])
plt.title("부산월평균 기온 - 전국 월평균 기온")
plt.xlabel('월')
plt.ylabel('기온차이(℃)')
plt.bar(month, diff)
for i in range(len(month)):
    height = diff[i]
    plt.text(month[i], 0, '%.1f' %height, ha='center', va='bottom', size = 12)
plt.show()


#plt.title("2022년 전국/제주 월평균 기온 추이")
#plt.xlabel('월')
#plt.ylabel('기온(℃)')
#plt.plot(month,korea, color='red', label='전국') 
#plt.plot(month,busan, color='orange',label='제주')
#plt.legend()
#plt.show()

diff = []
for i in range(0,12):
    diff.append(jeju[i]-korea[i])
plt.title("제주월평균 기온 - 전국 월평균 기온")
plt.xlabel('월')
plt.ylabel('기온차이(℃)')
plt.bar(month, diff)
for i in range(len(month)):
    height = diff[i]
    plt.text(month[i], 0, '%.1f' %height, ha='center', va='bottom', size = 12)
plt.show()


korea_file.close()
seoul_file.close()
deajeon_file.close()
busan_file.close()
jeju_file.close()

        


# In[ ]:




