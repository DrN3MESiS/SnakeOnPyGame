# Author: Alan Maldonado
# Description: Snake Module

# *** Libraries ***
import sys
import pygame
import random

from block import Block

# Snake Class: This class will handle every property that the game requires for this character


class Snake:
    body = []
    turns = {}
    defColor = (0, 233, 255)

    def __init__(self, defPos, rows, w):
        self.grid_rows = rows
        self.width = w
        self.head = Block(defPos, rows=self.grid_rows, w=self.width)
        self.body.append(self.head)
        self.ownX = 0
        self.ownY = 1
        self.increaseLength()
        self.increaseLength()

    def render(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.render(surface, True)
            else:
                c.render(surface)

    def resetPos(self, newPos):
        self.head = Block(newPos, rows=self.grid_rows, w=self.width)
        self.body = []
        self.body.append(self.head)
        self.increaseLength()
        self.increaseLength()
        self.turns = {}
        self.ownX = 0
        self.ownY = 1

    def movement(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.ownX = -1
                    self.ownY = 0
                    self.turns[self.head.pos[:]] = [self.ownX, self.ownY]

                elif keys[pygame.K_RIGHT]:
                    self.ownX = 1
                    self.ownY = 0
                    self.turns[self.head.pos[:]] = [self.ownX, self.ownY]

                elif keys[pygame.K_UP]:
                    self.ownX = 0
                    self.ownY = -1
                    self.turns[self.head.pos[:]] = [self.ownX, self.ownY]

                elif keys[pygame.K_DOWN]:
                    self.ownX = 0
                    self.ownY = 1
                    self.turns[self.head.pos[:]] = [self.ownX, self.ownY]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                if c.ownX == -1 and c.pos[0] <= 0:
                    c.pos = (c.rows-1, c.pos[1])
                elif c.ownX == 1 and c.pos[0] >= c.rows-1:
                    c.pos = (0, c.pos[1])
                elif c.ownY == 1 and c.pos[1] >= c.rows-1:
                    c.pos = (c.pos[0], 0)
                elif c.ownY == -1 and c.pos[1] <= 0:
                    c.pos = (c.pos[0], c.rows-1)
                else:
                    c.move(c.ownX, c.ownY)

    def increaseLength(self):
        tail = self.body[-1]
        dx, dy = tail.ownX, tail.ownY

        if dx == 1 and dy == 0:
            self.body.append(
                Block((tail.pos[0]-1, tail.pos[1]), rows=self.grid_rows, w=self.width))
        elif dx == -1 and dy == 0:
            self.body.append(
                Block((tail.pos[0]+1, tail.pos[1]), rows=self.grid_rows, w=self.width))
        elif dx == 0 and dy == 1:
            self.body.append(
                Block((tail.pos[0], tail.pos[1]-1), rows=self.grid_rows, w=self.width))
        elif dx == 0 and dy == -1:
            self.body.append(
                Block((tail.pos[0], tail.pos[1]+1), rows=self.grid_rows, w=self.width))

        self.body[-1].ownX = dx
        self.body[-1].ownY = dy
