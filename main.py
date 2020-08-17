import pygame
from pygame import *
from button import *
from game import *

def main():
	"""
	Main game function. Called upon starting the game.
	"""

	# Initializing pygame
	pygame.init()
	pygame.font.init()

	# DISPLAY can be found in settings.py
	screen = display.set_mode(DISPLAY)

	display.set_caption("Game of Life")

	background = pygame.Surface(DISPLAY)
	background = background.convert()
	background.fill((0,0,0))

	timer = time.Clock()

	game = Game()

	# Game loop
	while True:
		# Sets framrate to max 60 fps
		timer.tick(60)

		for event in pygame.event.get():
			# Handle closing the game
			if event.type == pygame.QUIT:
				exit()
			else:
				# Sends events to game.py
				game.handleEvent(event)

		# Update game state
		game.update()

		# Displaying graphics
		screen.blit(background, (0,0))
		game.draw(screen)
		pygame.display.update()

if(__name__ == "__main__"):
	main()


# TODO all lists are static length, switch to arrays
# TODO figure out why bottom row of cells looks different