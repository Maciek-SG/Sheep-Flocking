# Sheep-Flocking
As part of my project on Collective Motion in 2D at Durham University. This repository features all the code used as well as some extras. 

The following code and equations display flocking motion with respect to alignment, cohesion and repulsion as well as methods 
for testing the strength of flocking via concepts of polarisation, expanse and homogeneity. 

As a visual representation of the strength of these three simple rules we show a video of a flock which obeys alignment, 
cohesion and repulsion in a bounded domain as made by https://github.com/meznak/boids_py. Importantly I've set the perception
radius to 100 and crowding radius to 15.

https://user-images.githubusercontent.com/104319886/165834791-7ba55205-7e40-47f6-b512-05a4b657366d.mp4

As you can see the motion is quite convincing and it's why when I decided to model this mathematically, I based my system of equations on 
these three conditions.

The flocking occurs on a bounded domain and my code is for a rectangle, a circle and an annulus as well as a set of code which generates
random positions and velocities for these domains.
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

 
This is a video of a flock which obeys alignment, cohesion and repulsion in a bounded domain as made by https://github.com/meznak/boids_py

https://user-images.githubusercontent.com/104319886/165834791-7ba55205-7e40-47f6-b512-05a4b657366d.mp4

