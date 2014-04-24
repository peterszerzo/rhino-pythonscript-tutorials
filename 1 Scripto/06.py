"""

Rhino Python Script Tutorial
Exercise 06

How about a spiral?
Let's set the number of points as n, at the very top.
  It's a good idea to have these numbers at the very beginning of the program.
    You'll find and modify them much more quickly, especially as your script grows.

"""

import rhinoscriptsyntax as rs

import math

def Main():
    
    n = 50
    radius0 = 3
    
    
    for i in range(0, n): # notice how range() accepts variables
    
    	# a little trick here: as i goes from 0 to n-1, k will go from 0 to 1
    	k = i / (n - 1) 
    	
    	# traverse the full circle
        angle = k * 2 * math.pi 
        
        # increase radius
        radius = radius0 * (1 + 0.5 * k)
        
        # and now, work that trigonometry
        rs.AddPoint([radius * math.cos(angle), radius * math.sin(angle),0])
        

Main()