#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 19:38:53 2019

@author: yuqiugan
"""


import matplotlib.pyplot as plt
import math
import numpy as np
dot_file = []

# get information from 
with open('tsp.txt','r') as file:
    
    data = file.readlines()
    
    for line in data:
        
        dot_file.append(line.split())

dot_pool = []

# put the data into a tuple as the data of dots
for dots in dot_file:
    
    X = dots[0]
    Y = dots[1]
    pair = (X,Y)
    dot_pool.append(pair)

# define the function to calculate the distance between two dots
def D(x1,x2,y1,y2):
    
    x_x = float((x1-x2)**2)
    y_y = float((y1-y2)**2)
    d = math.sqrt(x_x + y_y)
    
    return d

# select the start point
#start = dot_pool[0]

# find how many dots in the pool
n = len(dot_pool)

#first_dot = start

#dot_pool.remove(start)


path = 1000
record = []
p = 0
f = 0
i = 10000
list_key =[]
list_try =[]
arr = np.arange(1000)
list_history = []

while i > 0:
    p = 0
    np.random.shuffle(arr)
    
    dot_use = []

    while p < 1000:
        
        dot_use.append(dot_pool[arr[p]])
        #print(dot_use)
        p += 1
   
    n = 0
    total = 0
    while n<999:
        
        first_dot = dot_use[n]
        second_dot = dot_use[n+1]

        
        # get the cordinate of the dots
        x1 = float(first_dot[0])
        y1 = float(first_dot[1])
        x2 = float(second_dot[0])
        y2 = float(second_dot[1])


        # do the calculate
        distancex = D(x1,x2,y1,y2)

        
        # accumulate distance
        total += distancex

        n += 1

    if total < path:
        
        path = total
        
        list_result = dot_use
    f += 1   
    list_history.append([float(f),float(path)])
   

    i -= 1

Z = 0
list_x = []
list_y = []
while Z < 1000:
    list_x.append(float(list_result[Z][0]))
    list_y.append(float(list_result[Z][1]))
    Z += 1

list_hx = []
list_hy = []
H = 0
while H < 10000:
    list_hx.append(float(list_history[H][0]))
    list_hy.append(float(list_history[H][1]))
    H += 1
fileobject = open('RS5.txt','w')   

for i in list_hy:
    
    fileobject.write(str(i))
    
    fileobject.write('\n')
    
fileobject.close()

plt.figure()
plt.plot(list_x,list_y,linewidth = 0.4, marker = 'o', markersize = 4, markerfacecolor = 'r')
plt.savefig('Path5.jpg')
plt.figure()
plt.plot(list_hx,list_hy)
plt.savefig('Generation5.jpg')

print(path)
