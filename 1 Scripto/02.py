"""

Rhino Python Script Tutorial
Exercise 02

Draw two points, and this time, name them.
  This is called assigning them to variables.
  
We make use of this here right away!
  When we draw a line between the two points, we use these names as references.
  
Feel free to change the coordinates and see what happens.  

"""

import rhinoscriptsyntax as rs

import math

def Main():
    
    p1 = rs.AddPoint([0,0,0])
    p2 = rs.AddPoint([0,0,2.5])
    
    rs.AddLine(p1, p2)

Main()