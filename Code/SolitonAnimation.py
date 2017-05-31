import numpy as np
from Soliton import soliton

def soliton_animation(x, theta, t0, tFin=None, dt=1e-1):
	""" 
	Get animation function which plots a soliton with 
	rapidity theta over 1D array x from time t0 to tFin 
	with time step dt
	"""
	from matplotlib import pyplot as plt
	from matplotlib import animation
	fig = plt.figure()
	ax = fig.gca()

	# set up plot at t=t0
	plt.xlabel('$x$', size=16)
	plt.ylabel('$u(x)$', size=16)
	u0 = soliton(x,t0,theta)
	line, = plt.plot(x, u0)
	tLabel = plt.text(0.05, 0.9, '', transform=ax.transAxes, size=16)

	def update_plot(i):
		# update time and time label
		t = t0 + dt*i
		tLabel.set_text('$t= %.2f$' % t)

		# update line
		u = soliton(x,t,theta)
		line.set_data(x, u)

	if tFin is None:
		frames = None
	else:
		frames = int((tFin-t0)/dt)

	# draw new frame every interval=1 milliseconds
	# the FuncAnimation instance needs to persist so it has to be assigned to a variable
	anim = animation.FuncAnimation(fig, update_plot, frames, interval=1)
	return anim

def show_soliton_animation(*args, **kwargs):
	from matplotlib import pyplot as plt
	anim = soliton_animation(*args, **kwargs)
	plt.show()

def save_soliton_animation(x, theta, t0, tFin, dt=1e-1):
	from matplotlib import pyplot as plt
	from matplotlib import animation

	# anim = animation.FuncAnimation(fig, animatingFunc, frames=int(tFin/dt), interval=1)
	writer = animation.FFMpegWriter(bitrate=1000, fps=60)

	anim = soliton_animation(x,theta,t0,tFin,dt)
	anim.save('solitonAnimation.mov', writer=writer)
	plt.close()

if __name__ == '__main__':
	from matplotlib import pyplot as plt
	x = np.linspace(-5,15,1001)
	t0, tFin, theta = -10, 60, 0.2
	show_soliton_animation(x,0.2,-5,60)
	# save_soliton_animation(x, theta, t0, tFin)

	##### create placeholder for animation
	# u = soliton(x, t0, theta)
	# plt.plot(x, u)
	# plt.xlabel('$x$', size=16)
	# plt.ylabel('$u(x)$', size=16)
	# plt.text(0.05, 0.9, '$t= %.2f$' % t0, transform=plt.gca().transAxes, size=16)
	# plt.savefig('solitonAnimationPlaceholder.pdf')
	
