import pygame
from pygame import *
from settings import *

class Cell:
	"""
	The cell object Conway's Game of Life
	"""

	alive = False
	alivenext = False
	neighbours = 0
	x,y = 0,0

	def __init__(self, x, y):
		# Screen position of cell in x, y coordinates
		self.x = x
		self.y = y
		# CELLSIZE found in settings.py
		self.rect = Rect(x,y,CELLSIZE,CELLSIZE)


	def mouseover(self, mpos):
		"""
		Checks if mosue is hovering over the cell.
		"""
		
		if self.x < mpos[0] < self.x+CELLSIZE and self.y < mpos[1] < self.y+CELLSIZE:
			return True
		else:
			return False

	def __str__(self):
		msg = "alive = {}\nneighbours = {}\n".format(self.alive,self.neighbours)
		return msg