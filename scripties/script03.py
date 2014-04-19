"""

Rhino Python Script Tutorial
Exercise 03

For loops Level 1.
Draw a number of points at different altitudes using a simple for loop.

"""

import rhinoscriptsyntax as rs

import math

def Main():
    
    # this for loop makes every command defined inside it execute several times
    # in this case, i takes on values 0, 1, 2 and so on, all the way up to 10
    for i in range(0,10):
        # as i changes, the following points are drawn at different altitudes (z-coordinates)
        rs.AddPoint([0,0,i])
        
    """
    
    The above loop is equivalent to:
    rs.AddPoint([0,0,0])
    rs.AddPoint([0,0,1])
    rs.AddPoint([0,0,2])
    rs.AddPoint([0,0,3])
    rs.AddPoint([0,0,4])
    rs.AddPoint([0,0,5])
    rs.AddPoint([0,0,6])
    rs.AddPoint([0,0,7])
    rs.AddPoint([0,0,8])
    rs.AddPoint([0,0,9])
    rs.AddPoint([0,0,10])
    
    """

Main()