WIDTH = 600
HEIGHT = 800

DISPLAY = (WIDTH, HEIGHT)
HALF_WIDTH = int(WIDTH/2)
HALF_HEIGHT = int(HEIGHT/2)

# Leaving 200 at bottom for buttons, rest is for the grid
CELLSIZE = 20
GRIDSIZE = (int(WIDTH/CELLSIZE), int((HEIGHT-200)/CELLSIZE))
ROWS = GRIDSIZE[0]
COLS = GRIDSIZE[1]


WHITE = (255,255,255)
GRAY = (120,120,120)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)

PATH = "./sprites/"
