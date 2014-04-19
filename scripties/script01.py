"""

Rhino Python Script Tutorial
Exercise 01

Draw point at origin.
Note: Python is sensitive to indentation.

"""

import rhinoscriptsyntax as rs

import math

def Main():

	rs.AddPoint([0,0,0])

Main()