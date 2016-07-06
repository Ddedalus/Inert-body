import numpy as np
from math import cos, sin


class Line:
	def __init__(self, mass, momentum, position=[0.0, 0.0], direction=[1, 0],
				velocity=[0.0, 0.0], angular_vel=1, time=0.0):

		self.m, self.I = float(mass), float(momentum)
		self.r = np.array([float(p) for p in position])
		self.n = np.array([float(n) for n in direction])
		self.v = np.array([float(v) for v in velocity])
		self.om = float(angular_vel)
		self.t = time
		self.new_pos = None		# should be defined as np.array's
		self.new_v = None

		def w(self):
			return np.matrix([[0, -1], [1, 0]]) * self.n

		def rotate(self, angle):
			r = np.matrix([[cos(angle), -sin(angle)],
			               [sin(angle), cos(angle)]])
			self.n = np.dot(r * self.n)

		def steiner(self, length):
			return self.I + self.m * length ** 2

class Point:
	def __init__(self, mass, position=[0.0, 0.0], velocity=[0.0, 0.0], time=0.0):
		self.m = mass
		self.r = np.array([float(p) for p in position])
		self.v = np.array([float(v) for v in velocity])
		self.t = float(time)
