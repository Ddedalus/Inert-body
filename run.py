# -*- coding: utf-8 -*-
from collider import *
from ploter import *
from Body import *
import copy

it = 20
point_0 = Point(1., [0., 0.], [1., 1.])
line_0 = Line(4., 4, [0., 0.], angular_vel=0)

# init_angle(point_0, line_0, math.pi / 5.0)
# plot_bodies(point_0, line_0, 'Initial position')

point, line = copy.copy(point_0), copy.copy(line_0)
switch_to_masspoint(point, line)


# point_r, line_r = copy.copy(point_0), copy.copy(line_0)
# switch_to_masspoint(point_r, line_r) # - causes crash

data_line = [line_0]
data_point = [point_0]

for i in range(it):
	point, line = collide(point, line)
	data_line.append(line)

Plotter.live = False

plot_bodies(point_0, line_0, 'Initial position')
plot_single_path(pos_inertial, 'Inertial path')
plot_single_path(pos_rigid, 'Rigid path')
plot_compare_paths(pos_rigid, pos_inertial)