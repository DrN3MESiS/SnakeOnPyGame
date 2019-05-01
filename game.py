# Author: Alan Maldonado
# Class: Plugin Development
# Description: Snake Game on PyGame

# *** Libraries ***
import sys
import pygame as engine
from snake import Snake

# Initialize the game engine and properties declaration
engine.init()
WindowConfig = width, height = 1000, 1000

# Initialize window
window = engine.display.set_mode(WindowConfig)
