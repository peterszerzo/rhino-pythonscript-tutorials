"""

Rhino Python Script Tutorial
Exercise 04

More for.

Let's work with this some more.
This is a parabola.

"""

import rhinoscriptsyntax as rs

import math

def Main():
    
    for i in range(0,10):
        rs.AddPoint([5 * i, 0.6 * i * i, 0])

Main()