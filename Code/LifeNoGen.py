"""
Conway's game of life with periodic boundary conditions
Inspired by https://jakevdp.github.io/blog/2013/08/07/conways-game-of-life/
XXX: This version does not use generators
"""
import numpy as np


def life_step(state):
	"""
	Takes a step in Conway's game of life with periodic boundary conditions
	"""
	# For every cell each live cell in any of the 8 neighbouring cells contributes 1 to the sum
	# Rolling matricies is periodic so this implements periodic boundary conditions
	numberOfNeigbours = sum(np.roll(np.roll(state, i, axis=0), j, axis=1)
						    for i in (-1,0,1) for j in (-1,0,1) if (i != 0 or j != 0))

	# Any live cell with fewer than two live neighbours dies, as if caused by under-population
	state = np.where(numberOfNeigbours < 2, 0, state)
	# Any live cell with more than three live neighbours dies, as if by over-population
	state = np.where(numberOfNeigbours > 3, 0, state)
	# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
	state = np.where(numberOfNeigbours == 3, 1, state)

	return state


def game_of_life(initialState, saveFile=None):
	from matplotlib import pyplot as plt
	import matplotlib.animation as animation

	image = plt.imshow(initialState, interpolation = 'nearest', cmap='Greys')
	plt.savefig('lifePlaceholder.pdf')

	def update_image(i):
		image.set_array(life_step(image.get_array()))

	fig = plt.gcf()

	if saveFile is None:
		imAnimation = animation.FuncAnimation(fig, update_image, interval=300)
		plt.show()

	else:
		imAnimation = animation.FuncAnimation(fig, update_image, frames=100, interval=300)
		writer = animation.FFMpegWriter(bitrate=1000, fps=3)
		imAnimation.save(saveFile, writer=writer)
		plt.close()

def interactive_game_of_life(initialState):
	from matplotlib import pyplot as plt
	import matplotlib.animation as animation

	fig = plt.figure()
	image = plt.imshow(initialState, interpolation = 'nearest', cmap='Greys')

	# need to declare global variables in functions to modify them
	global PAUSE 
	PAUSE = False

	def update_image(i):
		if not PAUSE:
			image.set_array(life_step(image.get_array()))

	# disable some default matplotlib shortcuts
	plt.rcParams['keymap.save'] = ''
	plt.rcParams['keymap.yscale'] = ''

	def on_keyPress(event):
		global PAUSE

		if event.key == ' ':
			# space pauses the animation
			PAUSE = not PAUSE

		saveFile = 'life.npy'
		if event.key == 's':
			print('Saving to %s' % saveFile)
			image.get_array().dump(saveFile)
			print('Saved')

		elif event.key == 'l':
			print('Loading %s' % saveFile)
			state = np.load(saveFile)
			image.set_array(state)
			print('Loaded')

		# update pause text
		if PAUSE:
			pauseLabel.set_text('Paused')
		else:
			pauseLabel.set_text('')

	axis = plt.gca()
	pauseLabel = plt.text(0.42, 1.02, '', transform=axis.transAxes, size=16)

	def on_click(event):
		if event.button == 1:
			# on left click
			x, y = event.xdata, event.ydata

			if x is not None and y is not None:
				x, y = int(round(x)), int(round(y))

				# flip selected tile
				state = image.get_array()
				state[y,x] = (state[y,x] + 1) % 2
				image.set_array(state)


	fig = plt.gcf()
	imAnimation = animation.FuncAnimation(fig, update_image, interval=300)
	fig.canvas.mpl_connect('button_press_event', on_click)
	fig.canvas.mpl_connect('key_press_event', on_keyPress)

	plt.show()
if __name__ == '__main__':
	X = np.zeros((4,5))
	X[2,1:4] = 1
	print(X)
	print(life_step(X))


	Y = np.zeros((60,60))

	toad = [[1, 1, 1, 0],
	        [0, 1, 1, 1]]

	glider = [[0, 1, 0, 0],
	          [0, 0, 1, 0],
	          [1, 1, 1, 0]]

	pentadecathlon = [[1, 1, 1],
	          		  [1, 0, 1],
	          		  [1, 1, 1],
	          		  [1, 1, 1],
	          		  [1, 1, 1],
	          		  [1, 1, 1],
	          		  [1, 0, 1],
	          		  [1, 1, 1]]

	Y[2:4, 6:10] = toad
	Y[6:9, 46:50] = glider
	Y[20:28, 30:33] = pentadecathlon

	# game_of_life(Y, 'life.mov')
	interactive_game_of_life(Y)