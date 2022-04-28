# Sheep-Flocking
As part of my project on Collective Motion in 2D at Durham University. This repository features all the code used as well as some extras. 

The following code and equations display flocking motion with respect to alignment, cohesion and repulsion as well as methods 
for testing the strength of flocking via concepts of polarisation, expanse and homogeneity. 
The flocking occurs on a bounded domain and my code is for a rectangle, a circle and an annulus as well as a set of code which generates
random positions and velocities for domains.
I also include some code which shows how to iterate and perform multiple tests for multiple generated initial conditions.

I would recommend playing around with the initial rectangular case, trying different functions to see how it works. I've included
the functions which I call the 'baseline' equations which will definitely work, but feel free to change all of these. 

I would not recommend using this code to witness the motion (many such already exist and are linked elsewhere) but instead
to look at snapshots, play around with the functions and to visually see if flocks and groups are formed and to investigate the 
'strength' of these flocks. 

If you want to make new boundaries and areas you just need to change the 'wall force' section, if unclear just check the differences between
the code given. 

These functions were based off of the Cucker-Smale and Three-Zone model.

I also include some extra results which were implied, but not necessarily shown in my paper.

We also have the video example of collective motion in 2D from the Boids program which utilises the three rules listed above. 
