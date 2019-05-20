# Author: Alan Maldonado
# Description: Blocks Module

# *** Libraries ***

import sys
import pygame

# Block Class
# Contains: - In-game Objects to Render


class Block(object):

    # Block Class Initializer
    def __init__(self, defPos, x=1, y=0, color=(177, 183, 0), rows=50, w=1000):
        self.rows = rows
        self.w = w
        self.pos = defPos
        self.ownX = x
        self.ownY = y
        self.color = color

    # Grid Moving Method
    def move(self, x, y):
        self.ownX = x
        self.ownY = y
        self.pos = (self.pos[0] + self.ownX, self.pos[1] + self.ownY)

    # Block rendering per object placed.
    def render(self, surface, eyes=False):
        dt = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color,
                         (i*dt+1, j*dt+2, dt-2, dt-2))
