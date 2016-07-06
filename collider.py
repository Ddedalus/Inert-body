# -*- coding: utf-8 -*-from Body import *
import numpy as np
from numpy.linalg import norm
import math
import copy, logging
from Body import Line, Point


def collide(line, point):
	l = copy.copy(line)
	p = copy.copy(point)

	t = math.arccos(np.dot(l.n, l.r)/norm(l.n) * norm(l.r))
	#check it!

	lb = 2 * l.m * p.m * l.steiner(norm(l.r)) * \
	     (l.v - p.v) \
	     / ((l.m + p.m) * l.steiner(norm(l.r)) + l.m * p.m * np.cross(l.r, l.w()))

	l.v += lb/l.m
	p.v -= lb/p.m
	l.om += lb/l.steiner(l.r) * np.cross(l.r, l.w())

	l.r += l.v * t
	p.r += p.v * t
	l.rotate(t * l.om[2])
	return l, p


def switch_to_masspoint(p, l):
	vx = (p.m * p.v[0] + l.m * l.v[0]) / (p.m + l.m)
	vy = (p.m * p.v[1] + l.m * l.v[1]) / (p.m + l.m)
	v = (p.v * p.m + l.v * l.m) / (p.m + l.m)
	x = (p.m * p.r[0] + l.m * l.r[0]) / (p.m + l.m)
	y = (p.m * p.r[1] + l.m * l.r[1]) / (p.m + l.m)
	pos = (p.r * p.m + l.r * l.m) / (p.m + l.m)
	for k in [p, l]:
		k.v = k.v - v
		k.r = k.r - pos

	print('Momentum:', p.v * p.m + l.v * l.m)
	print('Masspoint:', p.r * p.m + l.r * l.m)

def summary_momentum(bill, ring):
	return bill.v * bill.m + ring.v * ring.m


def run_inertial(bill, ring, it=10):
	pos_b = [bill.pos]
	rad_b = [np.linalg.norm(bill.pos)]
	b = copy.copy(bill)
	r = copy.copy(ring)
	switch_to_masspoint(b, r)

	for i in range(it):
		b, r = collide(b, r)
		pos_b.append(b.pos)
		# rad_b.append(np.linalg.norm(bill.pos))

	# print(pos_b[-1])
	# print('Radius:', bill.radius())

	return pos_b
