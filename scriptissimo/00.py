"""

Rhino Python Script Tutorial
Advanced

Exercise 00

Simulate particle-spring system.

"""

import rhinoscriptsyntax as rs

import math


particles = []
springs = []

nx = 10
ny = 10
	
ax = 10
ay = 20

dt = 0.01


class Particle:
	
	def __init__(self, x, y):
	
		self.position = [x, y, 0] 
		self.velocity = [0, 0, 0]
		self.freedom = [1, 1, 1]
		self.mass = [1, 1, 1]
		
	def fix(self):
		
		self.freedom = [0, 0, 0]
			
		
	def place(self):
	
		rs.AddPoint([self.position])
		
	
class Spring:
	
	def __init__(self, node_index_1, node_index_2):
		
		self.n1 = node_index_1
		self.n2 = node_index_2
		self.stiffness = 1
		self.restLength = 0
		
	def place(self):
		
		p1 = particles[self.n1].position
		p2 = particles[self.n2].position
		rs.AddLine(p1, p2)
		
	def 	
	

def Main():

	for ix in range(0, nx):
		for iy in range(0, ny):
			kix = ix / (nx - 1)
			kiy = iy / (ny - 1)
			p = Particle(ax * kix, ay * kiy)
			particles.append(p)
		
	for ix in range(0, nx):
		for iy in range(0, ny):
		
			if (ix < (nx - 1)):
				s = Spring(ix * nx + iy, (ix + 1) * nx + iy)
				springs.append(s)
				
			if (iy < (ny - 1)):
				s = Spring(ix * nx + iy, ix * nx + (iy + 1))
				springs.append(s)
	
	
	for spring in springs:
		spring.place()	

Main()