"""
Conway's game of life with periodic boundary conditions
Inspired by https://jakevdp.github.io/blog/2013/08/07/conways-game-of-life/
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

def life_generator(initialState):
	state = initialState
	paused = False
	while True:
		passedVal = yield state
		if passedVal is None:
			if not paused:
				state = life_step(state)
		elif passedVal == 'toggle pause':
			paused = not paused
		else:
			state = passedVal


def game_of_life(initialState):
	from matplotlib import pyplot as plt
	import matplotlib.animation as animation

	# cmap='Greys' maps values in [0,1] to colours between ['white', 'black']
	fig = plt.gcf()
	image = plt.imshow(initialState, interpolation = 'nearest', cmap='Greys')
	life = life_generator(initialState)

	def update_image(state):
		image.set_array(state)

	# pass frames a generator which will in turn pass to update_image each state
	imAnimation = animation.FuncAnimation(fig, update_image, frames=life, interval=300)
	plt.show()


def interactive_game_of_life(initialState):
	from matplotlib import pyplot as plt
	import matplotlib.animation as animation

	# cmap='Greys' maps values in [0,1] to colours between ['white', 'black']
	fig = plt.gcf()
	image = plt.imshow(initialState, interpolation = 'nearest', cmap='Greys')
	life = life_generator(initialState)


	def update_image(state):
		image.set_array(state)

	# disable some default matplotlib shortcuts
	plt.rcParams['keymap.save'] = ''
	plt.rcParams['keymap.yscale'] = ''

	axis = plt.gca()
	pauseLabel = plt.text(0.42, 1.02, '', transform=axis.transAxes, size=16)

	def on_keyPress(event):
		if event.key == ' ':
			# space pauses the animation
			life.send('toggle pause')
			if pauseLabel.get_text() == '':
				pauseLabel.set_text('Paused')
			else:
				pauseLabel.set_text('')

		saveFile = 'life.npy'
		if event.key == 's':
			print('Saving to %s' % saveFile)
			image.get_array().dump(saveFile)
			print('Saved')
		elif event.key == 'l':
			print('Loading %s' % saveFile)
			loadedState = np.load(saveFile)
			life.send(loadedState)
			print('Loaded')


	def on_click(event):
		if event.button == 1:
			# on left click
			x, y = event.xdata, event.ydata

			if x is not None and y is not None:
				x, y = int(round(x)), int(round(y))

				# flip selected tile
				state = image.get_array()
				state[y,x] = (state[y,x] + 1) % 2
				life.send(state)


	fig = plt.gcf()
	imAnimation = animation.FuncAnimation(fig, update_image, frames=life, interval=300)
	fig.canvas.mpl_connect('button_press_event', on_click)
	fig.canvas.mpl_connect('key_press_event', on_keyPress)

	plt.show()

if __name__ == '__main__':

	# demonstrate generator
	X = np.zeros((4,4))
	X[2,1:4] = 1

	life = life_generator(X)
	print('X', X)
	print('1st', next(life))
	print('2nd', next(life))
	print('3rd', next(life))

	Y = np.array([[0, 1, 0, 0],
	     		  [0, 0, 1, 0],
	     		  [1, 1, 1, 0],
	     		  [0, 0, 0, 0]])

	print('Y', Y)
	print('send Y', life.send(Y))
	print('1st  Y', next(life))


	A = np.zeros((60,60))

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

	A[2:4, 6:10] = toad
	A[6:9, 46:50] = glider
	A[20:28, 30:33] = pentadecathlon

	# game_of_life(A)
	interactive_game_of_life(X)