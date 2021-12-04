import numpy as np
from dataclasses import dataclass
from types import FunctionType
import pygame

box_size = 20

width, height = 1200, 800
maze_width, maze_height = 820, 800

pygame.font.init()
Font = pygame.font.SysFont('timesnewroman', box_size // 2)


class colors:
    white = (255, 255, 255)
    whitebg = (220, 220, 220)
    black = (20, 20, 60)
    yellow = (255, 255, 0)
    green = (0, 255, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    purple = (128, 0, 128)
    cyan = (0, 255, 255)
    gray = (122, 122, 122)
    dark_gray = (50, 50, 50)
    light_gray = (200, 200, 200)
    coral = (255, 127, 80)
    hot_pink = (255, 20, 147)
    lavender = (230, 230, 250)
    gold = (255, 215, 0)
    orange = (255, 165, 0)
    doger_blue = (30, 144, 255)
    rosy_brown = (188, 143, 143)
    dark_green = (34, 128, 34)


def find_minimum_g(node_list):
    cost_list = np.array([n.G_cost for n in node_list])
    idx = np.argmin(cost_list)
    return idx


def find_minimum_f(node_list):
    cost_list = np.array([n.F_cost for n in node_list])
    idx = np.argmin(cost_list)
    return idx


def find_neighbors(grid, node):
    steps = [-1, 0, 1]
    neighbours = []

    for step in steps:
        for s in steps:
            n_node = grid[node.column + s][node.row + step]
            neighbours.append(n_node)

    neighbours.pop(4)
    return neighbours


@dataclass
class Button:

    x: int
    y: int
    size: tuple
    color: tuple
    text: str
    functionality: FunctionType

    def check_pressed(self, pos):
        if pos[0] > self.x and pos[1] > self.y and pos[
                0] < self.x + self.size[0] and pos[1] < self.y + self.size[1]:
            return True
        return False


def draw_button(screen, button):

    pygame.draw.rect(screen, button.color,
                     (button.x, button.y, button.size[0], button.size[1]))
    font = pygame.font.SysFont('Corbel', 20)
    text = font.render(button.text, True, colors.black)
    screen.blit(text, (button.x + (button.size[0] // 2) - 5 * len(button.text),
                       button.y + button.size[1] // 2 - 10))


def wrap_reset(grid, clock):
    grid.full_reset()


def update_buttons(grid, clock, buttons, pos):
    for button in buttons:
        if button.check_pressed(pos):
            button.functionality(grid, clock)
