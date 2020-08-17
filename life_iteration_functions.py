from settings import *

def iter_life(cellarray):
	# Does one cycle of life according to the rules for Conway's Game of Life

	# Loops through cells and adds neighbours to each
	# ROWS and COLS found in settings.py
	for i in range(ROWS):
		for j in range(COLS):
			neighbourcount = 0
			# Sets neighbours to -1 to counteract itself being alive
			if cellarray[i][j].alive:
				neighbourcount -= 1
			# Loops through neighbours
			for n in range(-1,2):
				for m in range(-1,2):
					# Uses wrap-around when checking neighbours
					if cellarray[(i+n+ROWS)%ROWS][(j-m+COLS)%COLS].alive:
						neighbourcount += 1
			cellarray[i][j].neighbours = neighbourcount
	
	# Iterates through cells again to assigns which one is going to live
	for i in range(ROWS):
		for j in range(COLS):
			if cellarray[i][j].alive:
				if cellarray[i][j].neighbours > 3:
					cellarray[i][j].alivenext = False
				elif cellarray[i][j].neighbours < 2:
					cellarray[i][j].alivenext = False
				else:
					cellarray[i][j].alivenext = True
			else:
				if cellarray[i][j].neighbours == 3:
					cellarray[i][j].alivenext = True

	# Finally updates the alive state of each every cell
	for i in range(GRIDSIZE[0]):
		for j in range(GRIDSIZE[1]):
			if cellarray[i][j].alivenext:
				cellarray[i][j].alive = True
				cellarray[i][j].alivenext = False
			elif not cellarray[i][j].alivenext:
				cellarray[i][j].alive = False

	return cellarray