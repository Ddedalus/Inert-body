import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arrow


# matplotlib.use('Agg')


class Plotter:
	live = False


font = {'family': 'serif',
        'color': 'darkred',
        'weight': 'normal',
        'size': 16}


def plot_bodies(l, p, title='Position'):
	fig = plt.figure()
	plt.axis('equal')
	plt.title(title)
	ax = fig.add_subplot(111)

	a1 = Arrow( *l.r[:2], 5*l.n[0], 5*l.n[1], color='r', capstyle='round', width=0.5,
	            antialiased=True)
	l1 = Circle((l.r[0], l.r[1]), radius=0.1, fill=True, color='r')
	p1 = Circle((p.r[0], p.r[1]), radius=0.1, fill=True, color='g')
	p2 = Circle((0, 0), radius=0.1, fill=True, color='b')
	ax.add_patch(a1)
	ax.add_patch(p1)
	ax.add_patch(l1)
	ax.add_patch(p2)

	#add plot of omega!

	ax.autoscale_view()
	if Plotter.live is True:
		ax.figure.canvas.draw()
	else:
		plt.savefig('plot/position graph.png')
	plt.close()


def plot_single_path(pos_b, title=''):
	fig = plt.figure()
	plt.plot(*zip(*pos_b)[:2])
	plt.autoscale()
	plt.axis('equal')
	ax = fig.add_subplot(111)

	p1 = Circle(pos_b[0], radius=0.1, fill=True, color='b')
	plt.title("Path " + title)
	plt.xlabel('x')
	plt.ylabel('y')

	ax.add_patch(p1)
	if Plotter.live is True:
		plt.show()
	else:
		plt.savefig('plot/path single ' + title.lower() + '.png')

	plt.close()

def plot_vs_collision(data, title='Data'):
	plt.title(title + ' vs collision number')
	plt.plot(range(len(data) - 1), data)
	plt.axis('equal')
	plt.xlabel('collision')
	plt.ylabel(title.lower())
	if Plotter.live is True:
		plt.show()
	else:
		plt.savefig('plot/collision vs ' + title.lower() + '.png')
