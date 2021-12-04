import pygame
from util import *
from grid import *
from maze_generator import *
from maze_solver import *
from pygame import time


def main():

    pygame.init()

    clock = time.Clock()

    screen = pygame.display.set_mode((width, height))

    screen.fill(colors.doger_blue)

    grid = Grid(screen, (maze_width, maze_height), box_size)

    game_on = True

    #buttons
    buttons = []

    buttons.append(
        Button(int(width * 3 / 4), 100, (200, 60), colors.white, "Draw Maze",
               sidewinder_maze))

    buttons.append(
        Button(int(width * 3 / 4), 250, (200, 60), colors.white, "Solve A*",
               A_star))

    buttons.append(
        Button(int(width * 3 / 4), 400, (200, 60), colors.white, "Solve D*",
               Dijkstar))

    buttons.append(
        Button(int(width * 3 / 4), 550, (200, 60), colors.white, "Reset",
               wrap_reset))

    for button in buttons:
        draw_button(screen, button)

    while game_on:

        for event in pygame.event.get():

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if pos[0] > maze_width or pos[1] > maze_height:
                    update_buttons(grid, clock, buttons, pos)
                else:
                    grid.update_node(pos)

            if pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                if pos[0] < maze_width and pos[1] < maze_height:
                    x = (pos[0] // grid.box_size)
                    y = (pos[1] // grid.box_size)
                    grid.reset_node((x, y))

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    Dijkstar(grid, clock, True)

                if event.key == pygame.K_a:
                    A_star(grid, clock, True)

                if event.key == pygame.K_0:
                    sidewinder_maze(grid, clock)

            if event.type == pygame.QUIT:
                game_on = False

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
