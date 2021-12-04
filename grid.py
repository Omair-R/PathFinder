from util import colors, box_size, Font
import pygame
import numpy as np


class Node:

    G_cost = 0
    H_cost = 0
    F_cost = G_cost + H_cost

    is_begin = False
    is_end = False
    is_wall = False

    parent = None

    def __init__(self, screen, pos, size):
        self.screen = screen
        self.size = size

        self.x = pos[0] / size
        self.y = pos[1] / size

        self.column = pos[0] // size
        self.row = pos[1] // size

        self.xa = self.x * self.size
        self.ya = self.y * self.size

        self.color = colors.white

    def draw(self, border=False):

        self.change_color(colors.white, border=border)

    def change_color(self, color, display_cost=False, border=True):

        pygame.draw.rect(self.screen, color,
                         (self.xa, self.ya, self.size, self.size))

        if border:
            pygame.draw.rect(self.screen, colors.light_gray,
                             (self.xa, self.ya, self.size, self.size), 1)

        if display_cost:

            cost = Font.render(str(int(self.G_cost)), False, colors.dark_gray)
            self.screen.blit(cost,
                             (self.x * self.size + 4, self.y * self.size + 4))

    def calculate_g(self, grid):
        b = np.array([grid.start_node.column, grid.start_node.row])
        c = np.array([self.column, self.row])
        self.G_cost = np.linalg.norm(b - c) * 10
        pass

    def calculate_h(self, grid):
        a = np.array([grid.end_node.column, grid.end_node.row])
        c = np.array([self.column, self.row])
        self.H_cost = np.linalg.norm(a - c) * 10

    def calculate_f(self, grid):

        self.calculate_g(grid)
        self.calculate_h(grid)

        self.F_cost = self.G_cost + self.H_cost

    def set_begin(self):
        self.change_color(colors.doger_blue)
        self.is_begin = True

    def set_end(self):
        self.change_color(colors.dark_green)
        self.is_end = True

    def set_wall(self):
        self.change_color(colors.black, border=False)
        self.is_wall = True

    def reset(self):
        self.change_color(colors.white)
        self.parent = None
        if self.is_end: self.is_end = False
        if self.is_begin: self.is_begin = False
        if self.is_wall: self.is_wall = False


class Grid:

    nodes = []
    has_begin = False
    has_end = False
    start_node = None
    end_node = None

    def __init__(self, screen, window_size, box_size, lines=True):

        self.box_size = box_size
        self.width = window_size[0]
        self.height = window_size[1]
        self.screen = screen

        for i in range((self.width // box_size)):
            line = []

            for j in range(self.height // box_size):

                node = Node(screen, (i * box_size, j * box_size),
                            self.box_size)
                node.draw(border=lines)
                if i == 0 or j == 0 or i == (
                        self.width // box_size) - 1 or j == (self.height //
                                                             box_size) - 1:
                    node.set_wall()
                line.append(node)

            self.nodes.append(line)

    def __getitem__(self, key):
        return self.nodes[key]

    def __len__(self):
        return len(self.nodes)

    def update_node(self, pos):

        x = (pos[0] // self.box_size)
        y = (pos[1] // self.box_size)
        node = self.nodes[x][y]

        if not self.has_begin:
            node.set_begin()
            self.has_begin = True
            self.start_node = node

        elif not self.has_end and not node.is_begin:
            node.set_end()
            self.has_end = True
            self.end_node = node

        else:
            if not (node.is_begin or node.is_end): node.set_wall()

    def reset_node(self, box):

        node = self.nodes[box[0]][box[1]]

        if node.is_begin:
            self.has_begin = False
            self.start_node = None

        if node.is_end:
            self.has_end = False
            self.end_node = None

        node.reset()

    def full_black(self):
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes[0])):
                self.reset_node((i, j))
                self[i][j].set_wall()

    def full_reset(self):
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes[0])):
                if i == 0 or j == 0 or i == (
                        self.width // box_size) - 1 or j == (self.height //
                                                             box_size) - 1:
                    self[i][j].set_wall()
                else:
                    self.reset_node((i, j))

    def partial_reset(self):
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes[0])):
                if self[i][j].is_begin or self[i][j].is_end or self[i][j].is_wall:
                    continue
                else:
                    self.reset_node((i, j))
        
