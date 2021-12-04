from util import *
import pygame


def Dijkstar(grid, clock, display_cost=False):

    close = []
    open = []
    current = None

    grid.partial_reset()
    
    if not grid.has_begin or not grid.has_end: return

    open.append(grid.start_node)

    while True:

        idx = find_minimum_g(open)
        current = open[idx]
        open.pop(idx)
        close.append(current)

        if current.is_end: break

        if not current.is_begin:
            current.change_color(colors.gold, display_cost=display_cost)

        neighbors = find_neighbors(grid, current)

        for neighbor in neighbors:

            if neighbor in close or neighbor.is_wall:
                continue

            if not neighbor.is_end:
                neighbor.change_color(colors.coral, display_cost=display_cost)

            if not (neighbor in open):
                neighbor.parent = current
                neighbor.calculate_g(grid)
                open.append(neighbor)

        clock.tick(50)
        pygame.display.flip()

    while current.parent and len(open) != 0:
        if not current.is_end:
            current.change_color(colors.purple, display_cost=display_cost)
        current = current.parent


def A_star(grid, clock, display_cost=False):

    close = []
    open = []
    current = None
    
    grid.partial_reset()

    if not grid.has_begin or not grid.has_end: return

    open.append(grid.start_node)

    while True:

        if len(open) == 0:
            ### print something on screen
            """ To fix!!!! """
            break

        idx = find_minimum_f(open)
        current = open[idx]
        open.pop(idx)
        close.append(current)

        if current.is_end: break

        if not current.is_begin:
            current.change_color(colors.gold, display_cost=display_cost)

        neighbors = find_neighbors(grid, current)

        for neighbor in neighbors:

            if neighbor in close or neighbor.is_wall:
                continue

            if not neighbor.is_end:
                neighbor.change_color(colors.coral, display_cost=display_cost)

            if not (neighbor in open):
                neighbor.parent = current
                neighbor.calculate_f(grid)
                open.append(neighbor)

        clock.tick(50)
        pygame.display.flip()

    while current.parent and len(open) != 0:
        if not current.is_end:
            current.change_color(colors.purple, display_cost=display_cost)
        current = current.parent
