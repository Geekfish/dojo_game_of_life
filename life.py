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

LIVE = True
DEAD = False

NEIGHBOUR_ADJUSTMENTS = (-1, 1)


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


def apply_adjustments(coord):
    return filter(lambda x: 0 <= x < GRID_SIZE, [coord + adjustment for adjustment in NEIGHBOUR_ADJUSTMENTS])


def update_grid(grid):
    new_grid = list()

    for x, line in enumerate(grid):
        new_grid.append(list())

        for y, cell in enumerate(line):
            list_of_neighbours = [
                grid[_x][_y]
                for _y in apply_adjustments(y)
                for _x in apply_adjustments(x)
            ]
            num_of_neighbours = sum(map(int, list_of_neighbours))

            if num_of_neighbours == 3:
                new_cell = LIVE
            elif cell is LIVE and num_of_neighbours == 2:
                new_cell = LIVE
            else:
                new_cell = DEAD

            new_grid[x].append(new_cell)
    return new_grid


grid = create_grid()

while True:
    _ = os.system("clear")
    grid = update_grid(grid)
    display_grid(grid)
    sleep(1)
