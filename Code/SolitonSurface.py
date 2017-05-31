import numpy as np
from Soliton import soliton

def soliton_surface_fig(x,t,th):
	"""
	Return figure with the soliton function plotted as a surface
	x and t are 1D arrays and the soliton rapidity th is a float
	"""
	import matplotlib.pyplot as plt
	from mpl_toolkits.mplot3d import Axes3D

	# set up the 3D axis
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	ax.set_xlabel('$t$')
	ax.set_ylabel('$x$')
	ax.set_zlabel('$u(x,t)$')
	ax.text2D(0.05, 0.9, r'$\theta= %.2f$' % th, 
		transform=ax.transAxes, size=16)

	# T[i,j] = t[i], X[i,j] = x[j]
	T, X = np.meshgrid(t,x, indexing = 'ij')
	ax.plot_surface(T, X, soliton(X,T,th))
	return fig

if __name__ == '__main__':
	import matplotlib.pyplot as plt

	x = np.linspace(-5,15,201)
	t = np.linspace(0,60,301)
	th = 0.1

	fig = soliton_surface_fig(x,t,th)
	# fig.savefig('SolitonSurface.pdf', bbox_inches='tight')
	plt.show()