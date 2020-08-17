import pygame
from pygame import *

class Button(pygame.sprite.Sprite):
	"""
	Button class.

	Takes a string of text and puts it in a position 
	with a rectangle of interaction area applied.
	"""

	def __init__(self, text, pos):
		pygame.sprite.Sprite.__init__(self)

		# Load default font
		self.font = pygame.font.SysFont("SuperAwesomeHyperUltraGeniousFont",60)

		# Render text
		self.normal = self.font.render(text, 0, Color("#AAAAAA"))
		self.hover = self.font.render(text, 0, Color("#FFFFFF"))
		self.image = self.normal
		self.pos = pos
		self.rect = self.image.get_rect(topleft=pos)


	def mouseover(self, mpos):
		"""
		Check if mouse cursor hover over self and apply hover colour
		"""

		if self.rect.collidepoint(mpos):
			self.image = self.hover
			return True

		else:
			self.image = self.normal
			return False


	def new_text(self, text):
		self.normal = self.font.render(text, 0, Color("#AAAAAA"))
		self.hover = self.font.render(text, 0, Color("#FFFFFF"))
		self.image = self.normal
		self.rect = self.image.get_rect(topleft=self.pos)