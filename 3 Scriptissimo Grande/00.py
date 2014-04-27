"""

Rhino Python Script Tutorial
Advanced

Exercise 00

Simulate particle-spring system.
Work in Progress!

"""

import rhinoscriptsyntax as rs

import math

class Particle:
	
	
	def __init__(self, x, y):
	
		self.position = [x, y, 0]
		self.velocity = [0, 0, 0]
		self.force = [0, 0, 0]
		self.freedom = [1, 1, 1]
		self.mass = [1, 1, 1]
		
		
	def update_velocity(self, dt):
	
		v0 = (self.velocity[0] + self.force[0] / self.mass[0] * dt) * 1.0
		v1 = (self.velocity[1] + self.force[1] / self.mass[1] * dt) * 1.0
		v2 = (self.velocity[2] + self.force[2] / self.mass[2] * dt) * 1.0
		
		self.velocity = [v0, v1, v2]
		
	
	def freeze(self):
		self.velocity = [0, 0, 0]
		
		
	def update_position(self, dt):
	
		x0 = self.position[0] + self.velocity[0] * dt * self.freedom[0]
		x1 = self.position[1] + self.velocity[1] * dt * self.freedom[1]
		x2 = self.position[2] + self.velocity[2] * dt * self.freedom[2]
		
		self.position = [x0, x1, x2]	
			
		
	def fix_all(self):
		self.freedom = [0, 0, 0]
		
		
	def position_from(self, reference_particle):
	
		x = self.position
		x0 = reference_particle.position
	
		return [x[0] - x0[0], x[1] - x0[1], x[2] - x0[2]]
		
		
	def add_force(self, force, direction):
	
		f0 = self.force[0]	
		f1 = self.force[1]	
		f2 = self.force[2]	
		
		self.force = [f0 + force * direction[0], f1 + force * direction[1], f2 + force * direction[2]]
		
		
	def draw(self):
		rs.AddPoint(self.position)
		
		
	def kinetic_energy(self):
	
		ke = 0
		ke += self.mass[0] * self.velocity[0] ** 2	/ 2
		ke += self.mass[1] * self.velocity[1] ** 2	/ 2
		ke += self.mass[2] * self.velocity[2] ** 2	/ 2
		return ke
		
		
class Spring:
	
	def __init__(self, node_index_1, node_index_2):
		
		self.n1 = node_index_1
		self.n2 = node_index_2
		self.stiffness = 100
		self.vector = []
		self.length = 0		
		self.rest_length = 0
				
		
	def update(self, particles):
	
		spring_vector = particles[self.n2].position_from(particles[self.n1])	
		self.vector = spring_vector
		
		l = (spring_vector[0] ** 2 + spring_vector[1] ** 2 + spring_vector[2] ** 2) ** 0.5
		self.length = l
		
		self.force = self.stiffness * (self.length - self.rest_length)
		
		v0 = self.vector[0]	
		v1 = self.vector[1]	
		v2 = self.vector[2]
		
		self.vector = [v0 / l, v1 / l, v2 / l]
			
			
	def draw(self, particles):
	
		rs.AddLine(particles[self.n1].position, particles[self.n2].position)	
			

class ParticleSpringSystem:

	def __init__(self, name, dt = 0.001, tmax = 10000):
	
		self.name = name
		self.particles = []
		self.springs = []
		self.dt = dt
		self.t = 0
		self.tmax = tmax
		self.kinetic_energy = 0
		
		
	def add_particle(self, particle):
	
		self.particles.append(particle)
		
		
	def add_spring(self, spring):
	
		self.springs.append(spring)
		
		
	def draw(self):
	
		for spring in self.springs:
			
			spring.draw(self.particles)
			
		for particle in self.particles:
		
			if (particle.freedom[0] == 0):
				particle.draw()	
	
	
	def set_dynamics(self):
		
		for particle in self.particles:
			
			particle.force = [0, 0, 0]
			
		for spring in self.springs:
		
			spring.update(self.particles)
			self.particles[spring.n1].add_force(+ spring.force, spring.vector)
			self.particles[spring.n2].add_force(- spring.force, spring.vector)
			
			
	def advance_time_step(self):
	
		self.set_dynamics()
		
		kinetic_energy = 0
	
		for particle in self.particles:
			
			particle.update_velocity(self.dt)
			particle.update_position(self.dt)	
			
			kinetic_energy = kinetic_energy + particle.kinetic_energy()		

		if (kinetic_energy < self.kinetic_energy):
		
			for particle in self.particles:
			
				particle.freeze()
				self.kinetic_energy = 0
				
		else:
			
			self.kinetic_energy = kinetic_energy		
			

def Main():
	
	nx = 5
	ny = 5
	
	ax = 10
	ay = 10

	ps = ParticleSpringSystem("system1")
	
	for ix in range(0, nx):
	
		for iy in range(0, ny):
		
			kix = ix / (nx - 1)
			kiy = iy / (ny - 1)
			p = Particle(ax * kix, ay * kiy)
			
			if ((ix == 0 or ix == nx - 1) and (iy == 0 or iy == ny - 1)):
				p.fix_all()
			
			ps.add_particle(p)
			
					
	for ix in range(0, nx):
	
		for iy in range(0, ny):
						
			if (ix < (nx - 1)):
				spring1 = Spring( (ix + 0) * ny + (iy + 0), (ix + 1) * ny + (iy + 0) )
				spring1.update(ps.particles)
				spring1.rest_length = spring1.length * 0.8
				ps.add_spring(spring1)
				
			if (iy < (ny - 1)):
				spring2 = Spring( (ix + 0) * ny + (iy + 0), (ix + 0) * ny + (iy + 1) )
				spring2.update(ps.particles)
				spring2.rest_length = spring2.length * 0.8
				ps.add_spring(spring2)
	
	
	for i in range(0, 200):	
		ps.advance_time_step()
			
	ps.draw()
	
Main()