# Author: Alan Maldonado
# Description: Blocks Module

# *** Libraries ***

import sys
import pygame


class Block(object):
    rows = 50
    w = 1000

    def __init__(self, defPos, x=1, y=0, color=(177, 183, 0)):
        self.pos = defPos
        self.ownX = x
        self.ownY = y
        self.color = color

    def move(self, x, y):
        self.ownX = x
        self.ownY = y
        self.pos = (self.pos[0] + self.ownX, self.pos[1] + self.ownY)

    def render(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis-2))
