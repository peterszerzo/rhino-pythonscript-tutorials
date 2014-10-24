"""

Rhino Python Script Tutorial
Advanced

Exercise 01

Experiments on smart structures.

For conceptual background, see the following paper:
Glisic, B., Adriaenssens, S. and Szerzo, P. (2013), Structural Analysis and Validation of a Smart Pantograph Mast Concept. Computer-Aided Civil and Infrastructure Engineering.

"""

import rhinoscriptsyntax as rs

import math

class Pantograph:
	
	
	def __init__(self, n, l, c):
	
		self.n = n
		self.l = l
		self.c = c
		self.d = l / 3
		
		
	def draw(self):
	
		l1 = self.l
		y = 0
	
		for i in range(0, n):
			
			rs.AddLine([0, y, 0], [l1, y, 0])
			
			y += self.l / 3
			
			l1 *= (1 - self.c) / self.c
		

def Main():
	
    p  = Pantograph(10, 5, 0.5)
    
    p.draw()
    
	
Main()