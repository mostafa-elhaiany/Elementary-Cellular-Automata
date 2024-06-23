CELL_SIZE = (4, 4)  # Width and height of each cell
GRID_WIDTH = 350 # width of the 1D Cellular Automota
NUM_ITERS = 160
PROBA = .9 # percentage of zeros in iteration 0 (random generation)

#visualization
AS_CIRCLES = False
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


############## CONSTANTS ######################
# Calculate screen dimensions
GRID_DIMS = [GRID_WIDTH, NUM_ITERS]
SCREEN_WIDTH = CELL_SIZE[0] * GRID_DIMS[0]
SCREEN_HEIGHT = CELL_SIZE[1] * GRID_DIMS[1]
SCREEN_DIMS = (SCREEN_WIDTH, SCREEN_HEIGHT)
