"""

Rhino Python Script Tutorial
Advanced

Exercise 00

Analytical surfaces - the roof of the British Museum.

Bibliography:
	Williams, Christopher JK. "The analytic and numerical definition of the geometry of the British Museum Great Court Roof." (2001): 434-440.

"""

import rhinoscriptsyntax as rs

import math

nx = 30
ny = 30
	
ax = 80
ay = 80

a = 22
b = 36
c = 50
d = 50

def z2(x, y):
	r = (x ** 2 + y ** 2) ** 0.5
	z = (r / a - 1) * (1 - x / b) * (1 + x / b) * (1 - y / c) * (1 + y / d)
	return z

def Main():

	for ix in range(0, nx):
	
		for iy in range(0, ny):
		
			x = (ix / (nx - 1) - 0.5) * ax
			y = (iy / (ny - 1) - 0.5) * ay
			rs.AddPoint(x, y, 5 * z2(x, y))

Main()