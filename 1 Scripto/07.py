"""

Rhino Python Script Tutorial
Exercise 07

Let's spice up the spiral, and draw two this time!
Useful trick - if you have multiple geometries, you can automatically put them on different layers.
First you create them - using AddLayer.
Remember to switch between them accordingly, using CurrentLayer.

"""

import rhinoscriptsyntax as rs

import math

def Main():
    
    n = 50
    radius_0 = 3
    
    rs.AddLayer("spiral_1")
    rs.AddLayer("spiral_2")
    
    for i in range(0, n): # notice how range() accepts variables
    
    	# a little trick here: as i goes from 0 to n-1, k will go from 0 to 1
    	k = i / (n - 1) 
    	
    	# traverse the full circle
        angle = k * 3 * math.pi 
        
        # increase radius
        radius_1 = radius_0 * (1 + 5 * k)
        
        # increase radius
          # notice that the (1 - 4 * (k - 0.5) * (k - 0.5)) term is zero for k = 0 or 1
          	# and that it is 1 for k = 0.5
          # this term is responsible for separating the two spirals but having them meet at the endpoints	
        radius_2 = radius_0 * (1 + 5 * k) * (1 + 0.3 * (1 - 4 * (k - 0.5) * (k - 0.5)))
        
        rs.CurrentLayer("spiral_1")
        rs.AddPoint([radius_1 * math.cos(angle), radius_1 * math.sin(angle),0])
        
        rs.CurrentLayer("spiral_2")
        rs.AddPoint([radius_2 * math.cos(angle), radius_2 * math.sin(angle),0])
        

Main()