import numpy as np
import pygame
from grid import Grid


def sidewinder_maze(grid: Grid, clock):

    grid.full_black()

    for n in grid[1][1:-1]:
        n.reset()

    for n in np.arange(1, (len(grid) - 1))[2::2]:

        c = 1
        do = True

        for i in range(1, len(grid[0]) - 1):

            if do == False or i == len(grid[0]) - 2:
                do = True

            else:
                prop = np.random.randint(0, 10)
                do = True if prop <= 8 else False

            if do:
                grid[n][i].reset()

            else:
                if i > c:
                    j = np.random.randint(c, i)
                    grid[n - 1][j].reset()

                else:
                    grid[n - 1][i].reset()
                c = i + 1

            clock.tick(90)
            pygame.display.flip()

        if len(grid[0]) - 1 > c:
            j = np.random.randint(c, len(grid[0]) - 1)
            grid[n - 1][j].reset()
