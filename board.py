import pygame
from pygame import *
from cell import *
from settings import *
from life_iteration_functions import *

class Board:
	"""
	The board containing the cells.
	"""

	def __init__(self):
		self.cells = []

		# Constructs the board.
		for i in range(ROWS):
			self.cells.append([])
			for j in range(COLS):
				self.cells[i].append(Cell((i)*CELLSIZE, (j)*CELLSIZE))

		# PATH found in settings.py
		self.dead_image = pygame.image.load(PATH+"dead_cell.png")
		self.alive_image = pygame.image.load(PATH+"alive_cell.png")

		self.is_running = False


	def check(self, cell):
		"""
		Returns the corresponding image to the cells alive-state.
		"""
		if cell.alive:
			return self.alive_image
		else:
			return self.dead_image


	def iter_board(self):
		"""
		Iterates the board 1 life cycle.
		"""

		# iter_live found in life_iteration_functions.py
		self.cells = iter_life(self.cells)


	def clear(self):
		"""
		Sets all cells to the dead state.
		"""
		for cellarrays in self.cells:
			for cell in cellarrays:
				cell.alive = False


	def toggle_is_running(self):
		self.is_running = not self.is_running

