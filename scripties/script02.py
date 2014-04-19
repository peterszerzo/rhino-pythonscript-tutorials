"""

Rhino Python Script Tutorial
Exercise 02

Draw two points, and this time, store them in variables.
Use these variables to draw line between the points.

"""

import rhinoscriptsyntax as rs

import math

def Main():
    
    p1 = rs.AddPoint([0,0,0])
    p2 = rs.AddPoint([0,0,2.5])
    
    rs.AddLine(p1, p2)

Main()