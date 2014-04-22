"""

Rhino Python Script Tutorial
Exercise 01

Draw point at origin.
Important note: Python is very sensitive to indentation.
  Notice how the rs.AddPoint statement is indented inwards.
  This means that it is part of the Main method.
    All this will be clear in due time.

"""

import rhinoscriptsyntax as rs

import math

def Main():

	rs.AddPoint([0,0,0])

Main()