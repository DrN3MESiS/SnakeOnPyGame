# Author: Alan Maldonado
# Class: Plugin Development
# Description: Snake Game on PyGame

# *** Libraries ***
import sys
import pygame
from snake import Snake
import time
import random
from block import Block
import tkinter as tk
from tkinter import messagebox


class Game:
    pause = False
    died = False
    highScore = 0
    grid_color = (10, 0, 86)
    clock = pygame.time.Clock()
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (200, 0, 0)
    green = (0, 200, 0)
    bright_red = (255, 0, 0)
    bright_green = (0, 255, 0)

    def __init__(self, grid_rows, ms, window_width):
        self.grid_rows = grid_rows
        self.ms = ms
        self.width = window_width

        pygame.init()
        self.window = pygame.display.set_mode((self.width, self.width))
        pygame.display.set_caption('Snake Game: Alan Maldonado')
        # Scene Control
        self.game_intro()

    def game_intro(self):
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.window.fill(self.black)

            self.text_to_screen(
                self.window, 'Created by Alan Maldonado', 220, 20, size=20, color=self.green)
            self.text_to_screen(self.window, 'Snake', 175, 100, size=120)
            self.text_to_screen(self.window, '2K19', 100, 200, size=250)
            self.button(75, 450, 140, 50, self.bright_green,
                        self.green, self.start_game)
            self.button(400, 450, 100, 50, self.bright_red,
                        self.red, self.quit)
            self.text_to_screen(self.window, 'Play!', 115, 460, 42)
            self.text_to_screen(self.window, 'Quit', 415, 460, 42)
            pygame.display.flip()

    def game_pause(self):
        while self.pause:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.window.fill(self.white)
            self.text_to_screen(self.window, 'Game is paused',
                                35, 100, size=100, color=self.black)
            self.text_to_screen(self.window, 'Current score: ' + str(len(self.player.body) - 2),
                                110, 200, size=75, color=self.black)

            self.button(100, 450, 145, 50, self.bright_green,
                        self.green, self.unpause)
            self.button(400, 450, 100, 50, self.bright_red,
                        self.red, self.game_intro)
            self.text_to_screen(self.window, 'Continue!',
                                115, 460, 42)
            self.text_to_screen(self.window, 'Quit', 415, 460, 42)
            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(15)

    def unpause(self):
        self.pause = False

    def diedFunction(self):
        while self.died:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.window.fill(self.red)
            self.text_to_screen(self.window, 'YOU DIED',
                                160, 100, size=100, color=self.black)
            self.text_to_screen(self.window, 'Score: ' + str(len(self.player.body) - 2),
                                190, 200, size=75, color=self.white)

            self.text_to_screen(self.window, 'High Score: ' + str(self.highScore),
                                140, 300, size=75, color=self.white)

            self.button(80, 450, 200, 50, self.bright_green,
                        self.green, self.restart)
            self.button(400, 450, 100, 50, self.bright_red,
                        self.red,  self.quit)

            self.text_to_screen(self.window, 'Play Again?', 105, 460, 42)
            self.text_to_screen(self.window, 'Quit', 415, 460, 42)
            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(15)

    def restart(self):
        self.player.resetPos((10, 10))
        self.died = False
        pygame.display.update()

    def start_game(self):
        self.player = Snake((10, 10), self.grid_rows, self.width)
        self.RW = Block(self.createReward(), color=(
            255, 255, 255), rows=self.grid_rows, w=self.width)

        lock = True
        while lock:
            for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.pause = True
                        self.game_pause()
            pygame.time.delay(self.ms)
            self.clock.tick(10)
            self.player.movement()
            if self.player.body[0].pos == self.RW.pos:
                self.player.increaseLength()
                self.RW = Block(self.createReward(), color=(
                    255, 255, 255), rows=self.grid_rows, w=self.width)

            for x in range(len(self.player.body)):
                if self.player.body[x].pos in list(map(lambda z: z.pos, self.player.body[x+1:])):
                    if len(self.player.body) - 2 > self.highScore:
                        self.highScore = len(self.player.body) - 2
                    self.died = True
                    self.diedFunction()
                    pygame.display.update()
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

    def recreateScene(self, surface):
        surface.fill((7, 0, 58))
        self.player.render(surface)
        self.drawGrid(surface)
        pygame.draw.rect(self.window, self.red, (17, 20, 100, 15))
        pygame.draw.rect(self.window, self.red, (497, 20, 75, 15))
        self.text_to_screen(surface, 'High Score: ' +
                            str(self.highScore), 20, 20, size=20)
        self.text_to_screen(
            surface, 'Score: ' + str(len(self.player.body) - 2), 500, 20, size=20)
        pygame.display.flip()
        self.RW.render(surface)
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

    def text_to_screen(self, screen, text, x, y, size=50, color=(255, 255, 255)):
        text = str(text)
        font = pygame.font.Font(None, size)
        text = font.render(text, True, color)
        screen.blit(text, (x, y))

    def button(self, x, y, w, h, ic, ac, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(self.window, ac, (x, y, w, h))

            if click[0] == 1 and action != None:
                action()
        else:
            pygame.draw.rect(self.window, ic, (x, y, w, h))

    def quit(self):
        pygame.quit()
        quit()


start = Game(20, 0, 600)
# start = Game(50, 50, 600) #Default
pygame.quit()
quit()
