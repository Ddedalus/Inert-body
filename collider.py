# -*- coding: utf-8 -*-from Body import *
import numpy as np
from numpy.linalg import inv, norm
import math
import copy, logging
from Body import Line, Point


def collide_inertial(line, point):
	l = copy.copy(line)
	p = copy.copy(point)

	t = math.arccos(np.dot(l.n, l.r)/norm(l.n) * norm(l.r))
	#check it!

	lb = 2 * l.m * p.m * l.I * \
	     (l.v - p.v) \
	     / ((l.m + p.m) * l.I + l.m * p.m * np.cross(l.r, l.w()))

	l.v += lb/l.m
	p.v -= lb/p.m

	l.r += l.v * t
	p.r += p.v * t
	l.rotate(t * l.om)
	return l, p


def switch_to_masspoint(b, r):
	vx = (b.m * b.v[0] + r.m * r.v[0]) / (b.m + r.m)
	vy = (b.m * b.v[1] + r.m * r.v[1]) / (b.m + r.m)
	v = (b.v * b.m + r.v * r.m)/(b.m + r.m)
	x = (b.m * b.pos[0] + r.m * r.pos[0]) / (b.m + r.m)
	y = (b.m * b.pos[1] + r.m * r.pos[1]) / (b.m + r.m)
	pos = (b.pos * b.m + r.pos * r.m)/(b.m + r.m)
	for k in [b, r]:
		k.v = k.v - v
		k.pos = k.pos - pos

	print('Momentum:', b.v * b.m + r.v * r.m)
	print('Masspoint:', b.pos * b.m + r.pos * r.m)


def init_angle(bill, ring, fi=0, velocity=1.):
	# works properly in max range only with ring.pos=[0 0]
	y = ring.r * (1. - math.cos(2 * fi)) * 0.5
	x = - ring.r * math.sin(2 * fi) * 0.5
	# in coordinates according to ring's center

	bill.pos = np.array([x, y]) + ring.pos
	bill.v = np.array([math.sin(fi) * velocity, math.cos(fi) * velocity])

	if np.linalg.norm(ring.pos - bill.pos) > ring.r - bill.r:
		print('Warning: Angle over limit!', fi)
		return 1

	return 0


def summary_momentum(bill, ring):
	return bill.v * bill.m + ring.v * ring.m


def run_inertial(bill, ring, it=10):
	pos_b = [bill.pos]
	rad_b = [np.linalg.norm(bill.pos)]
	b = copy.copy(bill)
	r = copy.copy(ring)
	switch_to_masspoint(b, r)

	for i in range(it):
		b, r = collide_inertial(b, r)
		pos_b.append(b.pos)
		# rad_b.append(np.linalg.norm(bill.pos))

	# print(pos_b[-1])
	# print('Radius:', bill.radius())

	return pos_b
