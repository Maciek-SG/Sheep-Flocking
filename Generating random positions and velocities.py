# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 18:36:02 2022

@author: Junior
"""

from random import uniform
from math import pi
import numpy as np
import matplotlib.pyplot as plt


n=100 #number of sheep

v =[[uniform(-0.5,0.5),uniform(-0.5,0.5)] for i in range(n)] #generating random velocities
# print(v)

rectangularcoordinates = [[uniform(0,1000),uniform(0,800)] for i in range(n)] #generating rectangular coordinates
# print(rectangularcoordinates)



### Generating random positions on a circle ###

radius = 500
rc = [uniform(0,radius) for i in range(n)] #list of radii for circular field (max radius 500)
thetac = [uniform(0,2*pi) for i in range(n)] #list of theta

circularpos = [[((radius*rc[i])**0.5)*np.cos(thetac[i])+radius ,((radius*rc[i])**0.5)*np.sin(thetac[i])+radius] for i in range(n)]

# print(circularpos)

### Generating random positions on a annulus ###

outrad = 563 #radius of outer circle
inrad = 250 #radius of inner circle

    
ra = [uniform(inrad,outrad) for i in range(n)]   
a=inrad
b=outrad 
annularpos = [[(((((b**2)*((ra[i]-a)/(b-ra[i]))+a**2))/(1+((ra[i]-a)/(b-ra[i]))))**0.5)*np.cos(thetac[i]) +b ,(((((b**2)*((ra[i]-a)/(b-ra[i]))+a**2))/(1+((ra[i]-a)/(b-ra[i]))))**0.5)*np.sin(thetac[i])+b] for i in range(n)]


# print(annularpos)





x=[annularpos[i][0] for i in range(n)]
y=[annularpos[i][1] for i in range(n)]

# circle1 = plt.Circle((563, 563), 563, color='g',alpha=0.1)
# circle2 = plt.Circle((563, 563), 250, color='white',alpha=1)
# plt.figure(0)    
# # plt.gca().add_patch(circle1)
# # plt.gca().add_patch(circle2)
# plt.scatter(x,y,s=1)
# # plt.ylim(0,1200)
# # plt.xlim(0,1200)
# plt.gca().set_aspect('equal')
# plt.show()







