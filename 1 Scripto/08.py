"""

Rhino Python Script Tutorial
Exercise 08

Now that we stored the points in an array, we can use this array to draw lines between the points.

"""

import rhinoscriptsyntax as rs

import math

def Main():
    
    n = 50
    radius_0 = 3

    points = []
        
    for i in range(0, n): # notice how range() accepts variables
    
    	# a little trick here: as i goes from 0 to n-1, k will go from 0 to 1
    	k = i / (n - 1) 
    	
    	# traverse the full circle
        angle = k * 3 * math.pi 
        
        # increase radius
        radius = radius_0 * (1 + 5 * k)
                
        point = [radius * math.cos(angle), radius * math.sin(angle),0]

        # rs.AddPoint(point)

        points.append(point)

    for i in range(0, n-1):

        rs.AddLine(points[i], points[i + 1])
        
Main()