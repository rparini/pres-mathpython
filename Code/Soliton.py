from scipy import exp, cosh, sinh, arctan
def soliton(x,t,theta):
	"""
	One soliton solution of the sine-Gordon equation:
	u_{tt} - u_{xx} + sin(u) = 0
	with soliton rapidity theta
	"""
	z = cosh(theta)*x - sinh(theta)*t
	return 4*arctan(exp(z))

if __name__ == '__main__':
	from math import exp, cosh, sinh
	from math import atan as arctan

	# this works for single values of x,t
	print(soliton(1, 2, 0.2))

	# but we want to pass soliton a list of points and have it return a list of values
	# we could iterate over the list of x points and populate a list with the corresponding values
	u = []
	for x in [-1,-0.5,0,0.5,1]:
		u.append(soliton(x,2,0.2))

	# but much neater (and faster!) to use NumPy
	# note that we don't even have to redefine soliton
	from numpy import exp, cosh, sinh, arctan
	import numpy as np
	x = np.array([-1,-0.5,0,0.5,1], dtype='float64')
	u = soliton(x,2,0.2)

	##### create plot
	x  = np.linspace(-10,10,1001)
	t  = 3
	th = 0.2
	u = soliton(x, t, th)

	import matplotlib.pyplot as plt
	axis = plt.gca()
	plt.plot(x,u)
	plt.xlabel('$x$', size=16)
	plt.ylabel('$u(x)$', size=16)
	plt.text(0.05, 0.9, '$t= %.2f$' % t, transform=axis.transAxes, size=16)

	# save figure
	# plt.savefig('soliton.pdf', bbox_inches='tight')
	# plt.close()

	# show figure
	plt.show()





