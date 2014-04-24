"""

Rhino Python Script Tutorial
Advanced

Exercise 00

Simulate particle-spring system.

"""

import rhinoscriptsyntax as rs

import math

nx = 10
ny = 10
	
ax = 10
ay = 20

dt = 0.01

class Particle:
	
	def __init__(self, x, y):
	
		self.position = [x, y, 0]
		self.velocity = [0, 0, 0]
		self.force = [0, 0, 0]
		self.freedom = [1, 1, 1]
		self.mass = [1, 1, 1]
		
	def fix(self):
		
		self.freedom = [0, 0, 0]	
			
		
class Spring:
	
	def __init__(self, node_index_1, node_index_2):
		
		self.n1 = node_index_1
		self.n2 = node_index_2
		self.stiffness = 1
		self.restLength = 0
	
			

class ParticleSpringSystem:

	def __init__(self, name):
	
		self.name = name
		self.particles = []
		self.springs = []
		self.dt = 0.001
		self.t = 0
		self.tmax = 10000
		
		
	def addParticle(self, particle):
	
		self.particles.append(particle)
		
		
	def addSpring(self, spring):
	
		self.springs.append(spring)
		
		
	def draw(self):
	
		for spring in self.springs:
			
			rs.AddLine(self.particles[spring.n1].position, self.particles[spring.n2].position)		
	
	
	def setForce(self):
		
		for particle in self.particles:
			
			particle.force = [0, 0, 0]
			
		for spring in self.springs:
		
			i1 = spring.n1
			i2 = spring.n2
			
			dx = self.particles[i1].position[0] - self.particles[i2].position[0]
			dy = self.particles[i1].position[1] - self.particles[i2].position[1]
			dz = self.particles[i1].position[2] - self.particles[i2].position[2]
			
			d = (dx ** 2 + dy ** 2 + dz ** 2) ** 0.5


def Main():
	
	ps = ParticleSpringSystem("system1")
	
	for ix in range(0, nx):
		for iy in range(0, ny):
			kix = ix / (nx - 1)
			kiy = iy / (ny - 1)
			p = Particle(ax * kix, ay * kiy)
			ps.addParticle(p)
		
	for ix in range(0, nx):
		for iy in range(0, ny):
		
			if (ix < (nx - 1)):
				s = Spring(ix * nx + iy, (ix + 1) * nx + iy)
				ps.addSpring(s)
				
			if (iy < (ny - 1)):
				s = Spring(ix * nx + iy, ix * nx + (iy + 1))
				ps.addSpring(s)
	
	
	ps.draw()

Main()