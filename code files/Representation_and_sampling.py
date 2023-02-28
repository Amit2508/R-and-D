#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 10:57:59 2023

@author: amitgoel
"""

import pandas as pd
import matplotlib.pyplot as plt



#headers = ['Name', 'Age', 'Marks']

df = pd.read_csv('samples.csv')
df=df.drop(0)
df=df.drop(1)
# print(df)

df.columns = ['sample interval', 'signal', 'filtered']
# print(df)

list1 = df.filtered
list2 = df.signal
# print(list1)

plotting1 = []
# plotting2 = []
for i in list1:
    plotting1.append(float(i))

# for i in list2:
#     plotting2.append(float(i))

# print(type(plotting[0]))


# print(plotting)
# print(len(plotting))

x = []
for i in range(1,10000):
    x.append(i)
    

# plt.subplot(1,2,1)
# plt.plot(x, plotting1)
# plt.subplot(1,2,2)
# plt.plot(x, plotting2)


# df.set_index('Marks').plot()

# plt.show()

haar = []

count = 30
flag = 1

i = 1
while(i<= 10000-1):
    j = i
    
#     if(i == 10000-count+1):
#         for k in range(1, count):
#             haar.append(-1)
#         break
    while(i<= 10000-1 and i < j + count):
        
        haar.append(-1)
        i+=1
            
            
    while(i<= 10000-1 and i< j + (2*count)):
        haar.append(1)
        i+=1
    flag = - flag 

    
# print(haar)
# print(len(haar))
plt.figure(figsize=(40,26))
plt.plot(x, plotting1, label ="ecg signal")
plt.plot(x, haar, label ="haar")
plt.show()

print(plotting1)
print(haar)