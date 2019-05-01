# Author: Alan Maldonado
# Description: Snake Module

# *** Libraries ***
import sys
import pygame
import random

# Snake Class: This class will handle every property that the game requires for this character


class Snake:
    _length = int()

    def __init__(self, length):
        self._length = length
