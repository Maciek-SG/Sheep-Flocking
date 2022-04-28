# Sheep-Flocking
As part of my project on Collective Motion in 2D at Durham University. 
This repository features all the code used as well as some extras. 

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
I also include some code which shows how to iterate and perform multiple tests for multiple generated initial conditions as well as some extra results
which I did not include in my paper.

I would recommend playing around with the initial rectangular case, trying different functions to see how it works. I've included
the functions which I call the 'baseline' equations which will definitely work, but feel free to change all of these. 

I would not recommend using this code to witness the motion (many such already exist and are linked elsewhere) but instead
to look at snapshots, play around with the functions and to visually see if flocks and groups are formed and to investigate the 
'strength' of these flocks. 

If you want to make new boundaries and areas you just need to change the 'wall force' section, if unclear just check the differences between
the code given. 

These functions and systems were inspired by the Cucker-Smale and Three-Zone model.

**What to expect from this code**

Examples of results at time intervals of 0, 100, 1000, 10000:

![image](https://user-images.githubusercontent.com/104319886/165839036-c9d6efee-8da7-45a4-bd41-993dd4ee811c.png)

which yields the following:

![image](https://user-images.githubusercontent.com/104319886/165839090-d3a2d25c-af04-4447-9672-7feeff3b1715.png)

How these flocks visually look is completely dependent on how you set up the functions:

![image](https://user-images.githubusercontent.com/104319886/165837310-cc2944b2-fd2e-4d4c-a91c-dce902929bc4.png)
![image](https://user-images.githubusercontent.com/104319886/165837359-c4eaaf04-8ecd-447d-8c7a-760098287a18.png)

Play around with these and see what you can get. Adding noise would lead to even more crazy formations (and less symmetry).
I chose not to have noise to make analysis between different fields easier to do (since less randomness), but if you want 
to add it I would recommend changing the velocitycap function used in all so that it gives each sheep their own maximum
velocity since currently all my sheep travel at the same speed (which allows circular formations to form, we obviously
wouldn't see this in nature since different sheep have different top speeds). 

Also in this code I assumed the sheep have 360 degree vision. To remedy this you would have to adjust r as such 
![image](https://user-images.githubusercontent.com/104319886/165838018-b0ba22de-c6a7-457c-9351-60841dee1efd.png)

Unfortunately I only realised it would be this easy to implement towards the end. 

Thanks for reading!

![image](https://user-images.githubusercontent.com/104319886/165836371-1d6fd10e-4350-41f1-9f81-553c730f1d8e.png)
