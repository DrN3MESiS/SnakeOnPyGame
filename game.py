# Author: Alan Maldonado
# Class: Plugin Development
# Description: Snake Game on PyGame

# *** Libraries ***
import sys
import pygame
from snake import Snake
import random
from block import Block
import tkinter as tk
from tkinter import messagebox

# Functions


class Game:
    # Variables
    grid_rows = 50
    grid_color = (91, 117, 115)
    ms = 50
    clock = pygame.time.Clock()

    def __init__(self, grid_rows, ms):
        self.grid_rows = grid_rows
        self.ms = ms
        self.start_game()

    def start_game(self):
        # Initialize the game engine and properties declaration
        pygame.init()
        self.width = 1000

        # Initialize window
        self.window = pygame.display.set_mode((self.width, self.width))

        # Create Player
        self.player = Snake((10, 10))

        # Create reward object
        self.RW = Block(self.createReward(), color=(255, 255, 255))

        # Updating Scene
        lock = True
        while lock:
            pygame.time.delay(self.ms)
            self.clock.tick(10)
            self.player.movement()
            if self.player.body[0].pos == self.RW.pos:
                self.player.increaseLength()
                self.RW = Block(self.createReward(), color=(255, 255, 255))

            for x in range(len(self.player.body)):
                if self.player.body[x].pos in list(map(lambda z: z.pos, self.player.body[x+1:])):
                    print('Score:', len(self.player.body))
                    self.MSGBOX('You lost', 'Play again?')
                    self.player.resetPos((10, 10))
                    break

            self.recreateScene(self.window)

    def MSGBOX(self, sub, content):
        root = tk.Tk()
        root.attributes("-topmost", True)
        root.withdraw()
        messagebox.showinfo(sub, content)
        try:
            root.destroy()
        except:
            pass

    # Updating Window
    def recreateScene(self, surface):
        surface.fill((75, 91, 90))
        self.player.render(surface)
        self.RW.render(surface)
        self.drawGrid(surface)
        pygame.display.update()

    def createReward(self):
        positions = self.player.body
        while True:
            x = random.randrange(self.grid_rows)
            y = random.randrange(self.grid_rows)
            if len(list(filter(lambda z: z.pos == (x, y), positions))) > 0:
                continue
            else:
                break

        return (x, y)

    def drawGrid(self, Surface):
        sizeBtwn = self.width // self.grid_rows
        x = 0
        y = 0

        for i in range(self.grid_rows):
            x = x + sizeBtwn
            y = y + sizeBtwn

            pygame.draw.line(Surface, self.grid_color, (x, 0), (x, self.width))
            pygame.draw.line(Surface, self.grid_color, (0, y), (self.width, y))


start = Game(50, 50)
