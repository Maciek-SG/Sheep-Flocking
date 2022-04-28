# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 12:36:18 2022

@author: Junior
"""

import numpy as np
import math
import matplotlib.pyplot as plt



def V(r):           #repulsion at short distances, attraction at long (cohesion)
    return 3.5*(r+5)*math.log((r+5)/20)*np.exp(-((r+5)/25)**2)

    
def phi(r):         #positive everywhere and goes to 0 as r gets large - alignement 
    return (2.1*(0.2*r -0.4)**4)/np.exp(0.2*r -0.4)


def omega(x):     #gets larger the closer you get to 0 (closer sheep gets to wall)
    return 8*np.exp(-0.1*x)

def l(x):     #calculates distance from sheep to centre of circle (500,500)
    centre = np.array([500,500])    
    return np.subtract(centre,x)

def acceleration(x,v):     
    n = len(x)
    accelerationlist = []
    for i in range(n):
        w = l(x[i])
        a= np.zeros(2)
        for j in range(n):
            if i == j:
                pass
            else:
                r = np.linalg.norm(x[i]-x[j]) #the distance between i^th and j^th sheep
                
                a = np.add(a,(1/n)*phi(r)*np.add(v[i],v[j])) #alignement
                a = np.add(a,(1/n)*V(r)*(np.subtract(x[j],x[i])/r)) #repulsion/attraction
                a = np.add(a,omega(500-np.linalg.norm(w))*w/np.linalg.norm(w)) #wall force
        accelerationlist.append(a)
    return accelerationlist



def velocitycap(v): #takes all the velocities and ensures |v|<= 1
    n = len(v)
    for i in range(n):
        magnitude = np.linalg.norm(v[i])
        if magnitude <= 1:
            pass
        else:
            v[i] = (v[i] / magnitude)*1
    return v #returns the velocities which now all have magnitude <= 1

###### TESTING SECTION ######
def avg_pos(x):    # the average position of the flock    
    return np.sum(x, axis=0)/len(x)

def avg_vel(x):    # the average velocity of the flock
    return np.sum(x, axis=0)
def nearestneighbour(a,x,i):
    x = np.delete(x,i, axis = 0)    #gets rid of current vector in list to avoid getting 0 distance
    n = len(x)
    distances = []       # list filled with ther distances from a to ith vector
    for i in range(n):
        distances.append(np.linalg.norm(np.subtract(x[i],a)))
    distances = np.sort(distances)
    # print(distances)
    
    return [distances[0],distances[1]]   
def expanse(x):
    n = len(x)
    avg = avg_pos(x)
    ans = 0
    for i in range(n):
        ans += np.linalg.norm(np.subtract(avg,x[i]))
    
    return (ans / n)   #/ ((xdim**2 +ydim**2)**0.5)/2
def NND(x):    # the nearest neighbour distance
    n = len(x)
    n1 = 0
    n2 = 0
    for i in range(n):
        val = nearestneighbour(x[i],x,i)
        n1 += val[0]
        n2 += val[1]
    n1 = n1 / n
    n2 = n2 / n
    # print("n1 =",n1)
    # print("n2 =",n2)
    return (n2-n1) #/ (xdim**2 +ydim**2)**0.5
def polarisation(x):
    n = len(x)
    avg = avg_vel(x)
    ans = []
    
    for i in range(n):
        cosangle = np.dot(avg,x[i])/np.linalg.norm(x[i])/np.linalg.norm(avg)
        angle = np.arccos(cosangle)
        ans.append(angle)
        
    ans = np.sum(ans, axis=0)/n
    return  np.degrees(ans) #/ 90
    

##### TESTING SECTION FINISHED ######

def iterations(x,v,t): #time iterations     
    timelist = []
    NNDlist =[]
    expanselist = []
    polarisationlist =[]    
    for i in range(t):
        x = np.add(x,velocitycap(v))
        v = np.add(v,acceleration(x,v))
        
        # if i%10 == 0:    # comment out if just want to show sheep
        #     timelist.append(i)
        #     NNDlist.append(NND(x))
        #     expanselist.append(expanse(x))
        #     polarisationlist.append(polarisation(velocitycap(v)))
        
            
    return x , velocitycap(v), timelist, NNDlist, expanselist, polarisationlist


x=np.array() #list of sheep positions
v=np.array() #list of sheep velocities

t = 10000 #NUMBER OF TIMESTEPS

result = iterations(x,v,t)
finalpositions = result[0]
finalvelocities = result[1]
timelist = result[2]
NNDlist = result[3]
expanselist = result[4]
polarisationlist = result[5]


n=len(x)
x=[]
y=[]
for i in range(n):
    x.append(finalpositions[i][0])
    y.append(finalpositions[i][1])


circle = plt.Circle((500, 500), 500, color='g',alpha=0.1)
plt.figure(0)    
plt.gca().add_patch(circle)
plt.scatter(x,y)
plt.ylim(0,1000)
plt.xlim(0,1000)
# plt.gca().set_aspect('equal')
plt.show()

# print(timelist)
# print(NNDlist)
# print(expanse(finalpositions))

### STREGNTH OF FLOCKING STUFF ###

# plt.figure(1)
# plt.scatter(timelist,NNDlist, color = 'blue')
# plt.title("Homogeneity (Alignment Dominant)")
# plt.xlabel("Time-steps")
# plt.ylabel("NND (d)")
# plt.show()

# plt.figure(2)
# plt.scatter(timelist,expanselist ,color = 'red')
# plt.title("Compactness")
# plt.xlabel("Time-steps")
# plt.ylabel("Expanse")
# plt.show()

# plt.figure(3)
# plt.scatter(timelist,polarisationlist , color = 'green')
# plt.title("Coordination")
# plt.xlabel("Time-steps")
# plt.ylabel("Polarisation")
# plt.ylim(0,90)
# plt.show()





print("polarisation",polarisation(finalvelocities))
print("expanse",expanse(finalpositions))
print("homogeneity",NND(finalpositions))

    