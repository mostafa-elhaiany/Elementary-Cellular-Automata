import sys
import pygame
import config
import numpy as np
from Automata import ECA
# Initialize Pygame
pygame.init()

# Initialize screen
screen = pygame.display.set_mode(config.SCREEN_DIMS)
pygame.display.set_caption("Cellular Automata ")

grid = np.zeros((config.NUM_ITERS,config.GRID_WIDTH))

grid[0] = np.random.random((config.GRID_WIDTH,))
grid[grid>config.PROBA] = 1
grid[grid<1] = 0

simulating = False

def draw_grid(iteration):
    if(iteration>=config.NUM_ITERS): # animates the calculation of new states
        num_iters = config.NUM_ITERS
    else:
        num_iters = iteration
    for i in range(num_iters): 
        row = grid[i]
        for c_idx, c in enumerate(row):
            color = config.WHITE if c==1 else config.BLACK
            if(config.AS_CIRCLES):
                pygame.draw.circle(screen, color, (c_idx * config.CELL_SIZE[0], i * config.CELL_SIZE[1]), config.CELL_SIZE[0]//2)
            else:
                rect = pygame.Rect(c_idx * config.CELL_SIZE[0], i * config.CELL_SIZE[1], config.CELL_SIZE[0]-.5, config.CELL_SIZE[1]-.5)
                pygame.draw.rect(screen, color, rect)

def draw(iteration):
     # Fill screen with black
    screen.fill(config.BLACK)
    # draw grid        
    draw_grid(iteration)
    # Update display
    pygame.display.flip()

def randomize():
    """
    randomizes the grid
    """
    global grid, simulating
    grid = np.zeros((config.NUM_ITERS,config.GRID_WIDTH))
    grid[0] = np.random.random((config.GRID_WIDTH,))
    grid[grid>config.PROBA] = 1
    grid[grid<1] = 0
    simulating = False

def handle_event(event):
    """
    handling clicks and drags
    """
    global grid, simulating
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_r: # R to restart the simulation with random numbers
            randomize()
        elif event.key == pygame.K_SPACE: # toggle simulation
            simulating = not simulating

running = True
iteration = 1
automata = ECA(grid[0], config.RULE)
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            handle_event(event)
    draw(iteration)
    if simulating and iteration<config.NUM_ITERS:
        grid[iteration] = automata.update()
        iteration+=1
    elif(iteration>=config.NUM_ITERS):
        iteration = 1
        randomize()
        simulating = True

    clock.tick(60)
pygame.quit()
sys.exit()