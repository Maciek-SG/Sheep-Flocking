# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 12:36:18 2022

@author: Junior
"""

from random import uniform

###if you want to generate multiple sets of sheep at once and test h(3000) for all of them###

t = 3000 #number of timesteps
n1=100 #how many sheep
n2=10 #how many sets 
xlist = []
vlist = []
for i in range(n2):
    
    xlist.append([[uniform(0,1000),uniform(0,1000)] for j in range(n1)])
    vlist.append([[uniform(-0.5,0.5),uniform(-0.5,0.5)] for j in range(n1)])

hvalues = []

for i in range(n2):
    
    x = xlist[i]
    v = vlist[i]
    result = iterations(x,v,t)
    finalpositions = result[0]
    hvalues.append(NND(finalpositions))
    print('steps done=',i)
print(hvalues) #the values of h(3000) for all simulations
print(sum(hvalues)/len(hvalues)) #the average value of h(3000)



    