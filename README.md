The task is quiet easy to do with pymesh however pymesh only works with python3.6.
It is a really nice library that can do what you ask easily, however it does not work with python3.9.x .
I tried to do everything in a vritualbox with python3.6 installed but it messed my system up. 

Trimesh cannot read the .obj files and reads .stl files as scene object not trimesh object. Thus, I did not want to deal with it. I also tried openmesh and dmsh but I did not like them.

Finally, I decided to use triangle library in python3.9. The down side of this library it is a 2D mesh library. Therefore, I only explained the algorithm for vertices smaller than a threshold value in limit() function in main.py.

I only applied triangle mesh method to a square, but an option can be added to select any other shape that is defined in the code. 

More parser arguments can be added to enable/disable the conditions. 

######################
##### How to use #####
######################

python3 main.py -l <length> -a <area_limit> -d <degree_limit>

It will create two png files regarding the comparison of the applied conditions (Degree threshold first, area threshold second).

