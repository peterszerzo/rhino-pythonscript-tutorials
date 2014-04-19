"""

Rhino Python Script Tutorial
Exercise 04

For loops Level 2.

Draw points along a parabola.

"""

import rhinoscriptsyntax as rs

import math

def Main():
    
    for i in range(0,10):
        rs.AddPoint([5 * i, 0.6 * i * i, 0])

Main()