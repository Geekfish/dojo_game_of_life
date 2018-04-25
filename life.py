import os
import random
from time import sleep

"""
Rules of life:


    - Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.

    - Any live cell with two or three live neighbours lives on to the next generation.

    - Any live cell with more than three live neighbours dies, as if by overpopulation.

    - Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    
    
    Nice to haves:
    
    circular grid

"""

GRID_SIZE = 80

LIVE = 1
DEAD = 0

def create_grid():
    return [
        [random.choice([LIVE, DEAD]) for _ in range(GRID_SIZE)]
        for _ in range(GRID_SIZE)
    ]

def display_line(line):
    print(
        ''.join(("X" if cell is LIVE else " " for cell in line))
    )

def display_grid(grid):
    for line in grid:
        display_line(line)

def count_neighb_plus_self(grid,x,y):
    count = 0
    for xdif in [-1,0,1]:
        xn = x + xdif
        for ydif in [-1,0,1]:            
            yn = y + ydif
            if xn in range(GRID_SIZE) and yn in range(GRID_SIZE):
                count = count + grid[xn][yn]                
    return count

def live_or_dead(cell_state,count):
    if count == 3:
        return 1
    elif count < 3 or count > 4:
        return 0     
    elif count == 4:
        return 0 if cell_state == 0 else 1

def update_grid(grid):
    return [[live_or_dead(grid[x][y], count_neighb_plus_self(grid,x,y)) for y in range(GRID_SIZE)] for x in range(GRID_SIZE)]

#grid = testgrid
grid = create_grid()

while True:
    _ = os.system("clear")
    grid = update_grid(grid)
    display_grid(grid)
    sleep(1)
