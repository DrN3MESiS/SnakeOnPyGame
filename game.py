# Author: Alan Maldonado
# Class: Plugin Development
# Description: Snake Game on PyGame

# *** Libraries ***
import sys
import pygame
from snake import Snake

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
        self.player = Snake((0, 0))

        # Updating Scene
        lock = True
        while lock:
            pygame.time.delay(self.ms)
            self.clock.tick(10)
            self.recreateScene(self.window)
        pass

    # Updating Window
    def recreateScene(self, objWin):
        objWin.fill((75, 91, 90))
        self.drawGrid(objWin)
        pygame.display.update()

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
