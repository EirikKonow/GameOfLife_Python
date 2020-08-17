from button import *
from settings import *
from board import *

class Game:
	"""
	The main screen for the game.
	"""

	def __init__(self):
		# Buttons for the game screen
		self.btn_step = Button("Step", (int(WIDTH/4)-80,    HEIGHT-100))
		self.btn_clear = Button("Clear", (int(WIDTH/4)*2-65,  HEIGHT-100))
		self.btn_run = Button("Run", (int(WIDTH/4)*3-20, HEIGHT-100))
		# Adding buttons to a list for drawing
		self.buttons = [self.btn_step, self.btn_clear, self.btn_run]

		self.font = pygame.font.SysFont("SuperAwesomeHyperUltraGeniousFont",200)

		self.board = Board()


	def handleEvent(self, e):
		"""
		Handle events.
		"""

		# Drwas life in cells while mouse 1 is pressed.
		if pygame.mouse.get_pressed()[0]==1:
			for cellarray in self.board.cells:
				for cell in cellarray:
					if cell.mouseover(e.pos):
						cell.alive = True


		# Checking if buttons are clicked with mouse being realsed as trigger
		if e.type == MOUSEBUTTONUP:
			# Setps life 1 cycle if clicked
			if self.btn_step.mouseover(e.pos):
				self.board.iter_board()

			# Clears life on the whole board
			elif self.btn_clear.mouseover(e.pos):
				#btn2 code
				self.board.clear()

			# Toggles continously cycling life on board
			elif self.btn_run.mouseover(e.pos):
				self.board.toggle_is_running()
				if self.board.is_running:
					self.btn_run.new_text("Stop")
				else:
					self.btn_run.new_text("Run")

		# Update mouseover effect on buttons
		if e.type == MOUSEMOTION:
			for button in self.buttons:
				button.mouseover(e.pos)


	def update(self):
		"""
		Updates the game state.
		"""

		if self.board.is_running:
			self.board.iter_board()


	def draw(self, screen):
		"""
		Draws the game.
		"""
		
		for cellarray in self.board.cells:
			for cell in cellarray:
				screen.blit(self.board.check(cell), cell.rect)
		

		for button in self.buttons:
			screen.blit(button.image, button.rect)
	